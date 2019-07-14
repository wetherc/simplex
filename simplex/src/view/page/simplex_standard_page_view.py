from simplex.src.view.simplex_view import SimplexView
from simplex.src.view.layout import (
    simplex_header_view, simplex_sidebar_view,
    simplex_body_view)


class SimplexStandardPage(SimplexView):
    def __init__(self):
        self.classes = []
        self.header = simplex_header_view.SimplexHeader()
        self.sidebar = simplex_sidebar_view.SimplexSidebarView()
        self.body = simplex_body_view.SimplexBody()

    def render(self):
        standard_page = (
            self.render_head() +
            self.header.render() +
            self.sidebar.render() +
            self.body.render() +
            self.render_foot())

        return standard_page
