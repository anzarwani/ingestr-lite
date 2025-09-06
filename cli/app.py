# app.py
import typer
from ingest.runner import run_pipeline
from ingest.prefect_scheduler import deploy_prefect_flow

app = typer.Typer(help="Lite ETL tool with optional Prefect scheduling")

@app.command()
def run(config_path: str = typer.Argument(..., help="Path to YAML config file")):
    """
    Run the data pipeline locally.
    """
    typer.echo(f"Running pipeline with config: {config_path}")
    run_pipeline(config_path)

@app.command()
def schedule(config_path: str = typer.Argument(..., help="Path to YAML config file")):
    """
    Deploy the pipeline to Prefect scheduler based on the job config.
    """
    typer.echo(f"Scheduling pipeline with config: {config_path}")
    deploy_prefect_flow(config_path)

if __name__ == "__main__":
    app()
