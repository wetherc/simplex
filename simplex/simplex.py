from werkzeug.contrib.fixers import ProxyFix
from flask import (
    Flask, render_template, request, url_for, Blueprint,
    json, jsonify, make_response, Response, Markup, redirect
)
import pandas as pd
from simplex import (
    SimplexPage, SIMUI, SimplexLayout, SimplexData,
    SIMPLEX_ENV
)
from .application.auth import auth
from simplex.route.index_view import index_view_bp
from simplex.route.data_view import data_view_bp


app = Flask(__name__)

app.config.from_object(__name__)
app.secret_key = 'super secret string'
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(index_view_bp)
app.register_blueprint(data_view_bp)
app.register_blueprint(auth.auth_bp)



@app.before_request
def check_fresh_install():
    if SIMPLEX_ENV.config['fresh_install']:
        # There's, I'm sure, A Better Way (tm), but for now
        # this at least works
        if request.endpoint not in ['static', 'auth.register']:
            return redirect(url_for('auth.register'))
    return


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
