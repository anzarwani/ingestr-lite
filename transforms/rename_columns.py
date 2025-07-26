class RenameColumns:
    def __init__(self, columns: dict, **kwargs):
        """
        columns: dict where key = old column name, value = new column name
        """
        self.columns = columns

    def apply(self, df):
        return df.rename(columns=self.columns)
