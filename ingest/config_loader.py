import yaml
import os
from dotenv import load_dotenv

load_dotenv()

def load_config(path: str) -> dict:
    with open(path, "r") as f:
        raw_yaml = f.read()

    expanded_yaml = os.path.expandvars(raw_yaml)
    return yaml.safe_load(expanded_yaml)