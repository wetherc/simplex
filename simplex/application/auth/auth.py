from flask import Blueprint, render_template, url_for
from simplex import SIMUI, SimplexLayout
from .view import AuthRegistrationView


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/register')
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
            .set_href(url_for('auth.register'))
            .set_selected(True)
            .get_tag_content()
        )]

    page = AuthRegistrationView.RegistrationPageView()
    page.sidebar.items = _sidebar_items
    return render_template('index.html', content=page.render())
