import pandas as pd
import pytest
import wandb
from wandb.apis.importers import ImportConfig, WandbImporter


@pytest.mark.timeout(300)
def test_wandb_runs(wandb_server_src, wandb_server_dst, wandb_logging_config):
    # Import
    importer = WandbImporter(
        src_base_url=wandb_server_src.server.base_url,
        src_api_key=wandb_server_src.user,
        dst_base_url=wandb_server_dst.server.base_url,
        dst_api_key=wandb_server_dst.user,
    )

    config = ImportConfig(
        entity=wandb_server_dst.user,
        project=wandb_logging_config.project_name,
    )
    runs = importer.collect_runs(wandb_server_src.user)
    importer.import_runs(runs, config)

    # Check if import was successful
    api = wandb.Api(
        api_key=wandb_server_dst.user,
        overrides={"base_url": wandb_server_dst.server.base_url},
    )

    runs = api.runs(f"{config.entity}/{config.project}")
    runs = list(runs)

    assert len(runs) == wandb_logging_config.n_experiments
    for run in runs:
        history = run.scan_history()
        df = pd.DataFrame(history)
        metric_cols = df.columns.str.startswith("metric")
        media_cols = ["df", "img", "audio", "pc", "html", "plotly_fig", "mol"]

        metric_df = df.loc[:, metric_cols].dropna(how="all")
        media_df = df.loc[:, media_cols].dropna(how="all")

        assert metric_df.shape == (
            wandb_logging_config.n_steps,
            wandb_logging_config.n_metrics,
        )
        assert media_df.shape == (1, len(media_cols))


@pytest.mark.timeout(300)
def test_wandb_reports(wandb_server_src, wandb_server_dst, wandb_logging_config):
    # Import
    importer = WandbImporter(
        src_base_url=wandb_server_src.server.base_url,
        src_api_key=wandb_server_src.user,
        dst_base_url=wandb_server_dst.server.base_url,
        dst_api_key=wandb_server_dst.user,
    )

    config = ImportConfig(
        entity=wandb_server_dst.user,
        project=wandb_logging_config.project_name,
    )
    reports = importer.collect_reports(wandb_server_src.user)
    importer.import_reports(reports, config)

    # Check if import was successful
    api = wandb.Api(
        api_key=wandb_server_dst.user,
        overrides={"base_url": wandb_server_dst.server.base_url},
    )

    reports = api.reports(f"{config.entity}/{config.project}")
    reports = list(reports)

    assert len(reports) == wandb_logging_config.n_reports


@pytest.mark.timeout(300)
def test_wandb_artifact_sequence(
    wandb_server_src, wandb_server_dst, wandb_logging_config
):
    # Import
    importer = WandbImporter(
        src_base_url=wandb_server_src.server.base_url,
        src_api_key=wandb_server_src.user,
        dst_base_url=wandb_server_dst.server.base_url,
        dst_api_key=wandb_server_dst.user,
    )

    config = ImportConfig(
        entity=wandb_server_dst.user, project=wandb_logging_config.project_name
    )
    artifact_sequences = list(
        importer.collect_artifact_sequences(wandb_server_src.user, limit=1)
    )
    sequence = artifact_sequences[0]
    importer.import_artifact_sequence(sequence, config)

    # Check if import was successful
    api = wandb.Api(
        api_key=wandb_server_dst.user,
        overrides={"base_url": wandb_server_dst.server.base_url},
    )

    for source_art in sequence:
        result_art = api.artifact(source_art.name, source_art.type)
        assert result_art is not None

        assert result_art.name == source_art.name
        assert result_art.type == source_art.type
        assert result_art.description == source_art.description

        for name, result_entry in result_art.manifest.entries.items():
            source_entry = source_art.manifest.entries[name]
            assert result_entry.path == source_entry.path
            assert result_entry.digest == source_entry.digest
            assert result_entry.size == source_entry.size
