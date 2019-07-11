from werkzeug.contrib.fixers import ProxyFix
from flask import (
    Flask, render_template, request,
    json, jsonify, make_response, Response
)


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret string'
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/model_performance', methods=['GET', 'POST'])
def model_performance():
    if request.method == 'POST':
        
        return redirect(url_for('index'))

    return render_template('model_performance.html')

@app.route('/feature_distribution', methods=['GET', 'POST'])
def feature_distribution():
    if request.method == 'POST':
        
        return redirect(url_for('index'))

    return render_template('feature_distribution.html')