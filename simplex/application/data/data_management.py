import pandas as pd


class DataSummary():
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def preview(self):
        data = self.data

        return data.head()

    def summarize(self):
        summary = pd.DataFrame(self.data.dtypes)
        col_type = []
        for i in range(self.data.shape[1]):
            col_type.append(summary.iloc[i, 0])

        summarized_table = pd.concat([
            pd.DataFrame(self.data.columns),
            pd.DataFrame(col_type)],
            axis=1)
        summarized_table.columns = ['Feature', 'Data Type']

        return summarized_table
