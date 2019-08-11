class SIMUITableView():

    def __init__(self, table, header):
        self.table = table
        self.header = header

    def render_rows(self):
        joined_rows = ''
        header_content = ''.join(['<td>{}</td>'.format(
            self.header[i]) for i in range(self.table.shape[1])])
        header = '<tr>{}</tr>'.format(header_content)
        joined_rows += header
        for index, row in self.table.iterrows():
            row_content = ''.join(['<td>{}</td>'.format(
                row.iloc[i]) for i in range(self.table.shape[1])])
            rows = '<tr>{}</tr>'.format(row_content)
            joined_rows += rows

        return joined_rows

    def render(self):

        table = '<table>{}</table>'.format(self.render_rows())
        return table
