import requests
import pandas as pd


class APIReader:
    def __init__(self, url:str, method:str = "GET", headers:dict = None, params:dict=None, json_key:str = None):
        
        self.url = url 
        self.method = method.upper()
        self.headers = headers or {}
        self.params = params or {}
        self.json_key = json_key
        
    def read(self):
        response = requests.request(self.method, self.url, headers=self.headers, params=self.params)
        response.raise_for_status()
        data = response.json()
        
        if self.json_key:
            data = data[self.json_key]
            
        df = pd.DataFrame(data)
        return df

