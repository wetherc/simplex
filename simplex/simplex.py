from werkzeug.contrib.fixers import ProxyFix
from flask import (
    Flask, render_template, request, url_for,
    json, jsonify, make_response, Response
)
from simplex.view.page.simplex_standard_page_view import SimplexStandardPage
from simplex.view.layout.simplex_sidebar_view import SimplexSidebarItem
from simplex.view.simui.simui_list_item_view import SIMUIListItemView


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret string'
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/', methods=['GET', 'POST'])
def index():
    _sidebar_items = [
        SimplexSidebarItem().add_content(
            SIMUIListItemView()
            .set_name('Some Header')
            .set_type('label')
            .set_selected(False)
            .get_tag_content()
        ),
        SimplexSidebarItem().add_content(
            SIMUIListItemView()
            .set_name('Manage Data')
            .set_type('href')
            .set_href(url_for('manage_data'))
            .set_selected(True)
            .get_tag_content()
        )]

    page = SimplexStandardPage()
    page.sidebar.items = _sidebar_items
    return render_template('index.html', content=page.render())


@app.route('/manage/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('manage/data.html')


@app.route('/manage/models', methods=['GET', 'POST'])
def manage_models():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('manage/models.html')


@app.route('/model_performance', methods=['GET', 'POST'])
def model_performance():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('compare/model_performance.html')


@app.route('/feature_distribution', methods=['GET', 'POST'])
def feature_distribution():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('compare/feature_distribution.html')
