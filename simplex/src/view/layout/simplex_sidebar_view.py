class SimplexSidebarItem():
    def __init__(self, classes, content):
        self.classes = []
        self.label = None
        self.content = None

    def add_class(self, _class):
        self.classes.append(_class)

    def add_content(self, content):
        self.content = content

    def render(self):
        sidebar_item = """
        <li class="{}">{}</li>
        """.format(
            ' '.join(self.classes),
            self.content
        )
        return sidebar_item


class SimplexSidebarView():
    def __init__(self):
        self.menu_id = None
        self.classes = []
        self.items = [
            SimplexSidebarItem(
                classes=['side-menu-item', 'side-menu-item-selected'],
                content='Test'
            )
        ]

    def set_menu_id(self, menu_id):
        self.menu_id = menu_id

    def get_menu_id(self):
        return self.menu_id

    def add_class(self, _class):
        self.classes.append(_class)

    def add_menu_item(self, item: SimplexSidebarItem):
        self.items.append(item)

    def render(self):
        sidebar_view = """
        <div class="simplex-side-menu">
          <div class="side-menu-list-view">
            <ul class="side-menu">
              {}
            </ul>
          </div>
        </div>
        """.format(' '.join([item.render() for item in self.items]))
        return sidebar_view
