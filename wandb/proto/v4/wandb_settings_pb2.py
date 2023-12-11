# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wandb/proto/wandb_settings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n wandb/proto/wandb_settings.proto\x12\x0ewandb_internal\x1a\x1egoogle/protobuf/wrappers.proto\" \n\x0fListStringValue\x12\r\n\x05value\x18\x01 \x03(\t\"\x8a\x01\n\x17MapStringKeyStringValue\x12\x41\n\x05value\x18\x01 \x03(\x0b\x32\x32.wandb_internal.MapStringKeyStringValue.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcb\x01\n#MapStringKeyMapStringKeyStringValue\x12M\n\x05value\x18\x01 \x03(\x0b\x32>.wandb_internal.MapStringKeyMapStringKeyStringValue.ValueEntry\x1aU\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue:\x02\x38\x01\"\x9a\x01\n\x12OpenMetricsFilters\x12\x33\n\x08sequence\x18\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValueH\x00\x12\x46\n\x07mapping\x18\x02 \x01(\x0b\x32\x33.wandb_internal.MapStringKeyMapStringKeyStringValueH\x00\x42\x07\n\x05value\"\xaa\x43\n\x08Settings\x12.\n\x05_args\x18\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12/\n\x0b_aws_lambda\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x44\n\x1f_async_upload_concurrency_limit\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\x0e_cli_only_mode\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06_colab\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05_cuda\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\r_disable_meta\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10_disable_service\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15_disable_setproctitle\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0e_disable_stats\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f_disable_viewer\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x15_disable_machine_info\x18\x9e\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0c_except_exit\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\x0b_executable\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x44\n\x13_extra_http_headers\x18\x0e \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12:\n\x08_proxies\x18\xc8\x01 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12<\n\x16_file_stream_retry_max\x18\x93\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12I\n#_file_stream_retry_wait_min_seconds\x18\x94\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12I\n#_file_stream_retry_wait_max_seconds\x18\x95\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x41\n\x1c_file_stream_timeout_seconds\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12>\n\x18_file_transfer_retry_max\x18\x96\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12K\n%_file_transfer_retry_wait_min_seconds\x18\x97\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12K\n%_file_transfer_retry_wait_max_seconds\x18\x98\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x44\n\x1e_file_transfer_timeout_seconds\x18\x99\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x38\n\x14_flow_control_custom\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x16_flow_control_disabled\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x12_graphql_retry_max\x18\x9a\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x45\n\x1f_graphql_retry_wait_min_seconds\x18\x9b\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x45\n\x1f_graphql_retry_wait_max_seconds\x18\x9c\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12>\n\x18_graphql_timeout_seconds\x18\x9d\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12=\n\x17_internal_check_process\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12=\n\x17_internal_queue_timeout\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x08_ipython\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08_jupyter\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\r_jupyter_name\x18\x8f\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\r_jupyter_path\x18\x90\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\r_jupyter_root\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07_kaggle\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x17_live_policy_rate_limit\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12;\n\x16_live_policy_wait_time\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\n_log_level\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x34\n\x0f_network_buffer\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x05_noop\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\t_notebook\x18\x1d \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08_offline\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12)\n\x05_sync\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12)\n\x03_os\x18  \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\t_platform\x18! \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07_python\x18\" \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11_runqueue_item_id\x18# \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\r_require_core\x18$ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12_save_requirements\x18% \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x12_service_transport\x18& \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\r_service_wait\x18\' \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0f_start_datetime\x18( \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b_start_time\x18) \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\n_stats_pid\x18* \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12@\n\x1a_stats_sample_rate_seconds\x18+ \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x19_stats_samples_to_average\x18, \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x12_stats_join_assets\x18- \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12G\n!_stats_neuron_monitor_config_path\x18. \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12N\n\x1d_stats_open_metrics_endpoints\x18/ \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12G\n\x1b_stats_open_metrics_filters\x18\x30 \x01(\x0b\x32\".wandb_internal.OpenMetricsFilters\x12;\n\x11_stats_disk_paths\x18\x92\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12\x38\n\x12_stats_buffer_size\x18\xa1\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\r_tmp_code_dir\x18\x31 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\t_tracelog\x18\x32 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\r_unsaved_keys\x18\x33 \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12,\n\x08_windows\x18\x34 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10\x61llow_val_change\x18\x35 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\tanonymous\x18\x36 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x61pi_key\x18\x37 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12P\n\x1f\x61zure_account_url_to_access_key\x18\x38 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12.\n\x08\x62\x61se_url\x18\x39 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63ode_dir\x18: \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0c\x63onfig_paths\x18; \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12\x30\n\tcolab_url\x18\xa0\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x63onsole\x18< \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\ndeployment\x18= \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0c\x64isable_code\x18> \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0b\x64isable_git\x18? \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rdisable_hints\x18@ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14\x64isable_job_creation\x18\x41 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08\x64isabled\x18\x42 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x06\x64ocker\x18\x43 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x65mail\x18\x44 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x65ntity\x18\x45 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tfiles_dir\x18\x46 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x05\x66orce\x18G \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\ngit_commit\x18H \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\ngit_remote\x18I \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0egit_remote_url\x18J \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08git_root\x18K \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x11heartbeat_seconds\x18L \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x04host\x18M \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0cignore_globs\x18N \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12\x32\n\x0cinit_timeout\x18O \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x08is_local\x18P \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x08job_name\x18\x91\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\njob_source\x18Q \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rlabel_disable\x18R \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06launch\x18S \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x12launch_config_path\x18T \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07log_dir\x18U \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0clog_internal\x18V \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14log_symlink_internal\x18W \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10log_symlink_user\x18X \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08log_user\x18Y \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rlogin_timeout\x18Z \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12*\n\x04mode\x18\\ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rnotebook_name\x18] \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07problem\x18^ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07program\x18_ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x0fprogram_abspath\x18\x9f\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fprogram_relpath\x18` \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07project\x18\x61 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bproject_url\x18\x62 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x05quiet\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06reinit\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x07relogin\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x06resume\x18\x66 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cresume_fname\x18g \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07resumed\x18h \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\x08root_dir\x18i \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\trun_group\x18j \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06run_id\x18k \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0crun_job_type\x18l \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08run_mode\x18m \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08run_name\x18n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\trun_notes\x18o \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x08run_tags\x18p \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12-\n\x07run_url\x18q \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11sagemaker_disable\x18r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\tsave_code\x18s \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x0fsettings_system\x18t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12settings_workspace\x18u \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bshow_colors\x18v \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\nshow_emoji\x18w \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0bshow_errors\x18x \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\tshow_info\x18y \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rshow_warnings\x18z \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06silent\x18{ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0cstart_method\x18| \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x06strict\x18} \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0esummary_errors\x18~ \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x34\n\x0fsummary_timeout\x18\x7f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x10summary_warnings\x18\x80\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\x08sweep_id\x18\x81\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x10sweep_param_path\x18\x82\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\tsweep_url\x18\x83\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x07symlink\x18\x84\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x08sync_dir\x18\x85\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\tsync_file\x18\x86\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x13sync_symlink_latest\x18\x87\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rsystem_sample\x18\x88\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12;\n\x15system_sample_seconds\x18\x89\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12J\n%table_raise_on_max_row_limit_exceeded\x18\x8a\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x08timespec\x18\x8b\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x07tmp_dir\x18\x8c\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08username\x18\x8d\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\twandb_dir\x18\x8e\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wandb.proto.wandb_settings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._options = None
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_options = b'8\001'
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._options = None
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_options = b'8\001'
  _LISTSTRINGVALUE._serialized_start=84
  _LISTSTRINGVALUE._serialized_end=116
  _MAPSTRINGKEYSTRINGVALUE._serialized_start=119
  _MAPSTRINGKEYSTRINGVALUE._serialized_end=257
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_start=213
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_end=257
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE._serialized_start=260
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE._serialized_end=463
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_start=378
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_end=463
  _OPENMETRICSFILTERS._serialized_start=466
  _OPENMETRICSFILTERS._serialized_end=620
  _SETTINGS._serialized_start=623
  _SETTINGS._serialized_end=9241
# @@protoc_insertion_point(module_scope)
