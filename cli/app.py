# app.py
import typer
from ingest.runner import run_pipeline

def main(config_path: str = typer.Argument(..., help="Path to YAML config file")):
    """
    Run the data pipeline with the provided config.
    """
    typer.echo(f"Running pipeline with config: {config_path}")
    run_pipeline(config_path)

if __name__ == "__main__":
    typer.run(main)
