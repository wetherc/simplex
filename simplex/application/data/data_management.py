import pandas as pd
from simplex.view.simui import SIMUISelectItem
from simplex.view.simui import SIMUITable
# [TODO]: @brooke
# Use __init__ to abstract imports from underlying file hierarchy


class DataSummary():
    def __init__(self, data):
        self.data = data

    def preview(self):
        data = self.data.head()
        data = SIMUITableView(data, data.columns).render()

        return data

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

        options = [(
            SIMUISelectItemView()
            .set_select_options([
                'object',
                'float64',
                'int64',
                'datetime64',
                'bool',
                ])
            .set_selected_option(row['Data Type'])
            .set_id(row['Feature'])
            .render()) for index, row in summarized_table.iterrows()]

        summarized_table['Inputs'] = options
        summarized_table = summarized_table.loc[
            :, ['Feature', 'Inputs']].copy()
        table = SIMUITableView(
            summarized_table,
            summarized_table.columns).render()

        return table
