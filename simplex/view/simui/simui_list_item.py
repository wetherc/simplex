class SIMUIListItem():

    def __init__(self):
        self.name = None
        self.href = None
        self.type = 'href'
        self.is_external = False
        self.selected = False
        self.disabled = False
        self.open_in_new_window = False

    def set_name(self, name: str):
        self.name = name
        return self

    def set_href(self, href: str):
        self.href = href
        return self

    def set_type(self, type: str):
        self.type = type
        return self

    def set_is_external(self, is_external: bool):
        self.is_external = is_external
        return self

    def set_selected(self, selected: bool):
        self.selected = selected
        return self

    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self

    def set_open_in_new_window(self, open_in_new_window: bool):
        self.open_in_new_window = open_in_new_window
        return self

    def get_tag_attributes(self):
        classes = [f'side-menu-item-{self.type}']
        if self.selected:
            classes.append('side-menu-item-selected')

        if self.disabled:
            classes.append('side-menu-item-disabled')

        return ' '.join(classes)

    def get_tag_content(self) -> str:
        if self.type == 'href':
            return (
                f'<a class=\"{self.get_tag_attributes()}\"'
                f'href="{self.href}">'
                f'{self.name}</a>')
        else:
            return (
                f'<div class="{self.get_tag_attributes()}">'
                f'{self.name}</div>')
