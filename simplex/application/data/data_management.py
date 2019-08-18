import pandas as pd
from simplex.view.simui import SIMUISelectItem
from simplex.view.simui import SIMUITable
# [TODO]: @brooke
# Use __init__ to abstract imports from underlying file hierarchy


class DataSummary():
    def __init__(self, data):
        self.data = data

    def summarize(self):
        summary = pd.DataFrame(self.data.dtypes)
        col_type = []
        for i in range(self.data.shape[1]):
            col_type.append(summary.iloc[i, 0])

        summarized_table = pd.concat([
            pd.DataFrame(self.data.columns),
            pd.DataFrame(col_type)],
            axis=1)

        summarized_table.columns = ['Feature', 'Pandas Data Type']

        options = [(
            SIMUISelectItem()
            .set_select_options([
                'object',
                'float64',
                'int64',
                'datetime64',
                'bool',
                ])
            .set_selected_option(row['Pandas Data Type'])
            .set_id(row['Feature'])
            .render()) for index, row in summarized_table.iterrows()]

        summarized_table['Data Type'] = options
        summarized_table = summarized_table.loc[
            :, ['Data Type']].copy()
        # transpose the summary table
        summarized_table = summarized_table.transpose()
        # get preview table
        preview_table = self.data.head()
        # get consistent headers
        summarized_table.columns = preview_table.columns

        # combine two tables
        summarized_table = pd.concat([
            preview_table,
            summarized_table
        ], axis=0)

        table = SIMUITable(
            summarized_table,
            summarized_table.columns,
            'simplex-data-table').render()

        return table
