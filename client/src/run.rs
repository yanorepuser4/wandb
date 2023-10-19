use pyo3::prelude::*;

use crate::connection::Interface;
use crate::wandb_internal;
use chrono;
use rand::seq::SliceRandom;
use rand::thread_rng;
use std::collections::HashMap;
use tracing;

use crate::printer;
use crate::session::Settings;

// #[pyfunction]
pub fn generate_id(length: usize) -> String {
    // Using ASCII lowercase and digits to create a base-36 alphabet
    let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyz0123456789".chars().collect();
    let mut rng = thread_rng();

    (0..length)
        .map(|_| *alphabet.as_slice().choose(&mut rng).unwrap_or(&'a'))
        .collect()
}

#[pyclass]
pub struct Run {
    pub settings: Settings,
    pub interface: Interface,
}

impl Run {
    fn id(&self) -> String {
        self.settings.proto.run_id.clone().unwrap()
    }
}

#[pymethods]
impl Run {
    pub fn init(&mut self, id: Option<String>) {
        // generate a random string of length 8 if run_id is None:
        let run_id = match id {
            Some(id) => id,
            None => generate_id(8),
        };
        tracing::debug!("Initializing run {}", run_id);
        self.settings.proto.run_id = Some(run_id.clone());

        // generate timespec in YYYYMMDD_HHMMSS format
        let timespec = chrono::Local::now().format("%Y%m%d_%H%M%S").to_string();
        self.settings.proto.timespec = Some(timespec.clone());

        // if offline, "offline-run", else "run"
        let run_mode = if self.settings.proto.offline.is_some() {
            "offline-run".to_string()
        } else {
            "run".to_string()
        };
        self.settings.proto.run_mode = Some(run_mode.clone());

        // <get_cwd>/.wandb
        let wandb_dir = format!("{}/.wandb", std::env::current_dir().unwrap().display());
        self.settings.proto.wandb_dir = Some(wandb_dir.clone());

        self.settings.proto.sync_dir = Some(format!(
            "{}/{}-{}-{}",
            wandb_dir, run_mode, timespec, run_id
        ));

        let server_inform_init_request = wandb_internal::ServerRequest {
            server_request_type: Some(
                wandb_internal::server_request::ServerRequestType::InformInit(
                    wandb_internal::ServerInformInitRequest {
                        settings: Some(self.settings.proto.clone()),
                        info: Some(wandb_internal::RecordInfo {
                            stream_id: self.id(),
                            ..Default::default()
                        }),
                    },
                ),
            ),
        };

        self.interface
            .conn
            .send_message(&server_inform_init_request)
            .unwrap();

        let mut server_publish_run_request = wandb_internal::Record {
            record_type: Some(wandb_internal::record::RecordType::Run(
                wandb_internal::RunRecord {
                    run_id: self.id(),
                    // display_name: "gooba-gaba".to_string(),
                    info: Some(wandb_internal::RecordInfo {
                        stream_id: self.id(),
                        ..Default::default()
                    }),
                    ..Default::default()
                },
            )),
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };

        // update settings with backend's response
        let result = self
            .interface
            .conn
            .send_and_recv_message(&mut server_publish_run_request, &mut self.interface.handles);

        match result.result_type {
            Some(wandb_internal::result::ResultType::RunResult(run_result)) => {
                // TODO: this should be properly done in the settings module, like in python
                let run = run_result.run.unwrap();
                let entity = run.entity;
                let display_name = run.display_name;
                let project = run.project;
                self.settings.proto.entity = Some(entity.clone());
                self.settings.proto.project = Some(project.clone());
                self.settings.proto.run_name = Some(display_name.clone());

                let url = format!(
                    "https://wandb.ai/{}/{}/runs/{}",
                    entity,
                    project,
                    &self.id()
                );
                self.settings.proto.run_url = Some(url.clone());
            }
            Some(_) => {
                tracing::warn!("Unexpected result type");
            }
            None => {
                tracing::warn!("No result type, me is puzzled");
            }
        }

        let mut server_publish_run_start = wandb_internal::Record {
            record_type: Some(wandb_internal::record::RecordType::Request(
                wandb_internal::Request {
                    request_type: Some(wandb_internal::request::RequestType::RunStart(
                        wandb_internal::RunStartRequest {
                            run: Some(wandb_internal::RunRecord {
                                run_id: self.id(),
                                ..Default::default()
                            }),
                            info: Some(wandb_internal::RequestInfo {
                                stream_id: self.id(),
                                ..Default::default()
                            }),
                        },
                    )),
                },
            )),
            control: Some(wandb_internal::Control {
                local: true,
                ..Default::default()
            }),
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };
        let result = self
            .interface
            .conn
            .send_and_recv_message(&mut server_publish_run_start, &mut self.interface.handles);

        tracing::debug!("Result: {:?}", result);

        printer::print_header(&self.settings.run_name(), &self.settings.run_url());
    }

    pub fn log(&self, data: HashMap<String, f64>) {
        tracing::debug!("Logging to run {}", self.id());

        // TODO: make it work with steps
        // let history_record = wandb_internal::HistoryRecord {
        //     item: data
        //         .iter()
        //         .map(|(k, v)| wandb_internal::HistoryItem {
        //             key: k.clone(),
        //             value_json: v.to_string(),
        //             ..Default::default()
        //         })
        //         .collect(),
        //     ..Default::default()
        // };

        // let record = wandb_internal::Record {
        //     record_type: Some(wandb_internal::record::RecordType::History(history_record)),
        //     info: Some(wandb_internal::RecordInfo {
        //         stream_id: self.id.clone(),
        //         ..Default::default()
        //     }),
        //     ..Default::default()
        // };

        // let message = wandb_internal::ServerRequest {
        //     server_request_type: Some(
        //         wandb_internal::server_request::ServerRequestType::RecordPublish(record),
        //     ),
        // };

        // self.interface.conn.send_message(&message).unwrap();

        let partial_history_request = wandb_internal::PartialHistoryRequest {
            item: data
                .iter()
                .map(|(k, v)| wandb_internal::HistoryItem {
                    key: k.clone(),
                    value_json: v.to_string(),
                    ..Default::default()
                })
                .collect(),
            ..Default::default()
        };

        let record = wandb_internal::Record {
            record_type: Some(wandb_internal::record::RecordType::Request(
                wandb_internal::Request {
                    request_type: Some(wandb_internal::request::RequestType::PartialHistory(
                        partial_history_request,
                    )),
                },
            )),
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };

        let message = wandb_internal::ServerRequest {
            server_request_type: Some(
                wandb_internal::server_request::ServerRequestType::RecordPublish(record),
            ),
        };

        self.interface.conn.send_message(&message).unwrap();
    }

    pub fn finish(&mut self) {
        tracing::debug!("Finishing run {}", self.id());

        let finish_record = wandb_internal::RunExitRecord {
            exit_code: 0,
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };

        let mut record = wandb_internal::Record {
            record_type: Some(wandb_internal::record::RecordType::Exit(finish_record)),
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };

        self.interface
            .conn
            .send_and_recv_message(&mut record, &mut self.interface.handles);

        let mut shutdown_request = wandb_internal::Record {
            record_type: Some(wandb_internal::record::RecordType::Request(
                wandb_internal::Request {
                    request_type: Some(wandb_internal::request::RequestType::Shutdown(
                        wandb_internal::ShutdownRequest {
                            info: Some(wandb_internal::RequestInfo {
                                stream_id: self.id(),
                                ..Default::default()
                            }),
                        },
                    )),
                },
            )),
            info: Some(wandb_internal::RecordInfo {
                stream_id: self.id(),
                ..Default::default()
            }),
            ..Default::default()
        };

        let result = self
            .interface
            .conn
            .send_and_recv_message(&mut shutdown_request, &mut self.interface.handles);

        tracing::debug!("Result: {:?}", result);

        let inform_finish_request = wandb_internal::ServerRequest {
            server_request_type: Some(
                wandb_internal::server_request::ServerRequestType::InformFinish(
                    wandb_internal::ServerInformFinishRequest {
                        info: Some(wandb_internal::RecordInfo {
                            stream_id: self.id(),
                            ..Default::default()
                        }),
                    },
                ),
            ),
        };
        tracing::debug!("Sending inform finish request {:?}", inform_finish_request);
        self.interface
            .conn
            .send_message(&inform_finish_request)
            .unwrap();

        printer::print_footer(
            &self.settings.run_name(),
            &self.settings.run_url(),
            &self.settings.sync_dir(),
        );
    }
}