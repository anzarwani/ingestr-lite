from ingest.config_loader import load_config
from ingest.orchestrator import run_job


def run_pipeline(config_path:str):
    config = load_config(config_path)
    run_job(config)
    
    