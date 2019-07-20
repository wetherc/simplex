from flask import Markup
from simplex.view.simplex_view import SimplexView
from simplex.view.layout import (
    simplex_header_view, simplex_sidebar_view,
    simplex_body_view)


class SimplexStandardPage(SimplexView):
    def __init__(self):
        self.classes = []
        self.header = simplex_header_view.SimplexHeader()
        self.sidebar = simplex_sidebar_view.SimplexSidebarView()
        self.body = simplex_body_view.SimplexBody()

    def render_content_container(self):
        container = """
        <div class="simplex-standard-page-body">
        {}
        {}
        </div>
        """.format(
            self.sidebar.render(),
            self.body.render())

        return container

    def render(self):
        standard_page = (
            self.header.render() +
            self.render_content_container()
        )

        return Markup(standard_page)
