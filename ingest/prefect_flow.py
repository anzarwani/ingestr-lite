from prefect import flow
from ingest.runner import run_pipeline

@flow(log_prints=True)
def etl_flow(config_path: str):
    """Run ETL pipeline locally."""
    run_pipeline(config_path)
