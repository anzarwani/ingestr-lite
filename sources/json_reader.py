import pandas as pd


class JSONReader:
    def __init__(self, path, options=None, **kwargs):
        self.path = path 
        self.options = options or {}
        
        
    def read(self):
        return pd.read_json(self.path, **self.options)
    
    
    