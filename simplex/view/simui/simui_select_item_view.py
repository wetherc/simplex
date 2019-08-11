class SIMUISelectItemView():

    def __init__(self):
        self.options = []
        self.selected = None
        self.id = None

    def set_select_options(self, options: list):
        self.options = options

        return self

    def set_id(self, id: str):
        self.id = id

        return self

    def set_selected_option(self, selected: str):
        self.selected = selected

        return self

    def render(self):
        select_content = '<select id={}>{}</select>'.format(
            self.id,
            '\n'.join([
                f'<option>{option}</option>'
                if option != self.selected
                else f'<option selected>{option}</option>'
                for option in self.options
            ])
        )

        return select_content
