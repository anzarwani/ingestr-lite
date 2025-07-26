

class ChangeType:
    def __init__(self, columns: dict, **kwargs):
        """
        columns: dict where key = column name, value = target data type
        """
        self.columns = columns

    def apply(self, df):
        for col, dtype in self.columns.items():
            df[col] = df[col].astype(dtype)
        return df