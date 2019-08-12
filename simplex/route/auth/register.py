from flask import Blueprint, render_template, url_for
from simplex import (
    SimplexPage, SIMUI, SimplexLayout, SimplexData
)


register_bp = Blueprint('register', __name__)


@register_bp.route('/auth/register')
def register():
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
            .set_name('Register')
            .set_type('href')
            .set_href(url_for('register.register'))
            .set_selected(True)
            .get_tag_content()
        )]

    page = SimplexPage.SimplexStandardPage()
    page.sidebar.items = _sidebar_items
    return render_template('index.html', content=page.render())
