# ingest/prefect_scheduler.py
import yaml
import subprocess
from pathlib import Path
import typer

def generate_prefect_yaml(deployment_name: str, flow_entrypoint: str = "ingest.prefect_flow:etl_flow"):
    """
    Generates a minimal prefect.yaml for deployment.
    """
    content = {
        "name": deployment_name,
        "build": None,
        "push": None,
        "pull": [
            {"prefect.deployments.steps.set_working_directory": {"directory": str(Path.cwd())}}
        ],
        "deployments": [
            {
                "name": deployment_name,
                "entrypoint": flow_entrypoint,
                "parameters": {},
                "work_pool": {"name": "default", "work_queue_name": None},
                "schedules": [],
                "tags": [],
            }
        ],
    }

    with open("prefect.yaml", "w") as f:
        yaml.safe_dump(content, f)
    return "prefect.yaml"

def deploy_prefect_flow(job_config_path: str):
    """
    Reads the job config to determine deployment name and deploys it.
    """
    import yaml
    with open(job_config_path, "r") as f:
        job_conf = yaml.safe_load(f)
    deployment_name = job_conf["job"]["name"]

    typer.echo(f"Generating prefect.yaml for deployment '{deployment_name}'")
    generate_prefect_yaml(deployment_name)

    typer.echo("Deploying flow...")
    subprocess.run(f"prefect deploy -n {deployment_name}", shell=True, check=True)

    typer.echo("Ensure Prefect server is running and a worker exists:")
    typer.echo("  prefect server start")
    typer.echo("  prefect work-pool create --type process default")
    typer.echo("  prefect worker start --pool default")
