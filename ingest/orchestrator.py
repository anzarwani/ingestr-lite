from sources import csv_reader, excel_reader, json_reader
from destinations import postgres_writer
from transforms import drop_columns, change_type, rename_columns


TRANSFORM_REGISTRY = {
    "drop_columns":drop_columns.DropColumns,
    "change_type":change_type.ChangeType,
    'rename_columns':rename_columns.RenameColumns
}

SOURCE_REGISTRY = {
    "csv":csv_reader.CSVReader,
    "excel":excel_reader.ExcelReader,
    "json":json_reader.JSONReader
}

DESTINATION_REGISTRY = {
    "postgres":postgres_writer.PostgresWriter
}

def run_job(config: dict):
    source_conf = config["job"]["source"]
    dest_conf = config["job"]["destination"]
    transform_conf = config["job"].get("transformations", [])
    
    # Read data
    
    
    df = SOURCE_REGISTRY[source_conf["type"]](**source_conf).read()
    
    # Apply Transformation
    
    for t in transform_conf:
        transformer = TRANSFORM_REGISTRY[t["type"]](**t)
        
        df = transformer.apply(df)
        
    # Load to sink
    DESTINATION_REGISTRY[dest_conf["type"]](**dest_conf).write(df)