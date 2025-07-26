

class DropColumns:
    def __init__(self, columns, **kwargs):
        self.columns = columns 
        
        
    def apply(self, df):
        return df.drop(columns = self.columns)