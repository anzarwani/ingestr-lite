import pandas as pd


class ExcelReader:
    def __init__(self, path, options=None, **kwargs):
        self.path = path 
        self.options = options or {}
        
        
    def read(self):
        return pd.read_excel(self.path, **self.options)
    
    
    