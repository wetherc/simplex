from werkzeug.contrib.fixers import ProxyFix
from flask import (
    Flask, render_template, request, url_for,
    json, jsonify, make_response, Response, Markup
)
import pandas as pd
from simplex.application.data.data_management import DataSummary
# [TODO]: @brooke
# Use __init__ to abstract imports from underlying file hierarchy
from simplex import (
    SimplexManagement, SimplexStorage, Env,
    SimplexPage, SIMUI, SimplexLayout
)

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret string'
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/', methods=['GET', 'POST'])
def index():
    _sidebar_items = [
        SimplexLayout.SimplexSidebarItem().add_content(
            SIMUI.SIMUIListItemView()
            .set_name('Some Header')
            .set_type('label')
            .set_selected(False)
            .get_tag_content()
        ),
        SimplexLayout.SimplexSidebarItem().add_content(
            SIMUI.SIMUIListItemView()
            .set_name('Manage Data')
            .set_type('href')
            .set_href(url_for('manage_data'))
            .set_selected(True)
            .get_tag_content()
        )]

    page = SimplexPage.SimplexStandardPage()
    page.sidebar.items = _sidebar_items
    return render_template('index.html', content=page.render())


@app.route('/manage/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'POST':
        if 'data' not in request.files:
            flash('No file part')
        else:
            file = pd.read_csv(request.files.get('data'))
            file = DataSummary(file)
            preview_data = file.preview()
            summary_data = file.summarize()
            return render_template(
                'manage/data.html',
                data=Markup(preview_data),
                summary=Markup(summary_data))

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
