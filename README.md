# ingestr-lite

A minimal, flexible data ingestion engine written in Python. Inspired by [ingestr](https://github.com/bruin-data/ingestr) but simplified for rapid development, better readability, and ease of extension.

![Logo](./logo.png)

## Features

- Modular pipeline: **Source → Transform → Destination**
- Supports common file formats: CSV, JSON, Parquet
- Pluggable transformation steps (drop columns, cast types, custom logic)
- Load into PostgreSQL, AzureSQL DB (work in progress)
- Configurable via YAML and `.env` for secrets
- CLI interface using [Typer](https://typer.tiangolo.com/)
- Easy to extend with new sources, transforms, or writers

---

## Project Structure

```bash
liteingestor/
│
├── ingest/                     # Core pipeline orchestration
│   ├── __init__.py
│   ├── config_loader.py        # Parses YAML + environment variables
│   ├── orchestrator.py         # Main job runner (source → transform → sink)
│   ├── registry.py             # Maps type names to implementations
│   ├── runner.py               # Callable from CLI or external script
│
├── sources/                    # Source connectors
│   ├── __init__.py
│   ├── csv_reader.py
│
├── transforms/               # Data transformations
│   ├── __init__.py
│   ├── base.py                 # Abstract base class
│   ├── drop_columns.py         # drop columns
│
├── destinations/               # Destination writers
│   ├── __init__.py
│   ├── postgres_writer.py
│
├── cli/                        # Command-line interface
│   ├── __init__.py
│   ├── app.py                  # Typer CLI entrypoint
│
├── config/                     # Example configs
│   └── sample_config.yaml
│
├── tests/                      # Unit tests (pytest)
│   └── ...
|
├── main.py                     # For local execution
└── .gitignore


---
```


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/anzarwani/ingestr-lite.git
cd ingestr-lite

```

### 2. Install dependecies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a .env file in the root directory and add your database credentials:

```bash
POSTGRES_URI=postgresql://username:password@localhost:5432/<dbname>
```

### 4. Run your ingestion job

```bash
python cli/app.py config/sample_job.yaml
```

---

Feel free to contribute:

- Add source connectors
- Add destinations sinks




