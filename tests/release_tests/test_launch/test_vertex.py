import pytest
from utils import run_cmd_async
from wandb.sdk.launch.launch_add import launch_add

PROJECT = "release-testing"
ENTITY = "launch-release-testing"
JOB_NAME = "hello-world:v0"
QUEUE = "vertex-queue"


@pytest.mark.timeout(180)
def test_vertex_works():
    """Test that we can launch a run on Vertex AI."""
    queued_run = launch_add(
        queue_name=QUEUE,
        entity=ENTITY,
        project=PROJECT,
        job=f"{ENTITY}/{PROJECT}/{JOB_NAME}",
    )
    assert queued_run
    run_cmd_async(f"wandb launch-agent -q {QUEUE} -e {ENTITY}")
    queued_run.wait_until_finished()