import sqlalchemy


class PostgresWriter:
    def __init__(self, config, table, mode, **kwargs):
        self.uri = config['uri']
        self.table = table
        self.mode = mode
        
    def write(self, df):
        engine = sqlalchemy.create_engine(self.uri)
        
        df.to_sql(self.table, engine, if_exists = self.mode, index = False)