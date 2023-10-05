# Generated by wandb/proto/wandb_internal_codegen.py.  DO NOT EDIT!


import sys


if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


DEPRECATED_FEATURES = Literal[
    "keras_callback__data_type",
    "run__mode",
    "run__save_no_args",
    "run__join",
    "plots",
    "run__log_sync",
    "init__config_include_keys",
    "init__config_exclude_keys",
    "keras_callback__save_model",
    "langchain_tracer",
    "keras_callback__log_gradients"
]


class Deprecated:
    keras_callback__data_type: DEPRECATED_FEATURES = "keras_callback__data_type"
    run__mode: DEPRECATED_FEATURES = "run__mode"
    run__save_no_args: DEPRECATED_FEATURES = "run__save_no_args"
    run__join: DEPRECATED_FEATURES = "run__join"
    plots: DEPRECATED_FEATURES = "plots"
    run__log_sync: DEPRECATED_FEATURES = "run__log_sync"
    init__config_include_keys: DEPRECATED_FEATURES = "init__config_include_keys"
    init__config_exclude_keys: DEPRECATED_FEATURES = "init__config_exclude_keys"
    keras_callback__save_model: DEPRECATED_FEATURES = "keras_callback__save_model"
    langchain_tracer: DEPRECATED_FEATURES = "langchain_tracer"
    keras_callback__log_gradients: DEPRECATED_FEATURES = "keras_callback__log_gradients"
