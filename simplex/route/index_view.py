from flask import Blueprint, render_template, url_for
from simplex import (
    SimplexPage, SIMUI, SimplexLayout
)

index_view_bp = Blueprint('index_view', __name__)


@index_view_bp.route('/')
def index():
    _sidebar_items = [
        SimplexLayout.SimplexSidebarItem().add_content(
            SIMUI.SIMUIListItem()
            .set_name('Some Header')
            .set_type('label')
            .set_selected(False)
            .get_tag_content()
        ),
        SimplexLayout.SimplexSidebarItem().add_content(
            SIMUI.SIMUIListItem()
            .set_name('Manage Data')
            .set_type('href')
            .set_href(url_for('data_view.manage_data'))
            .set_selected(True)
            .get_tag_content()
        )]

    page = SimplexPage.SimplexStandardPage()
    page.sidebar.items = _sidebar_items
    return render_template('index.html', content=page.render())
