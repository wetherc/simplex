import pandas as pd
from flask import Blueprint, render_template, request, Markup
from simplex.application.data.data_management import DataSummary
# Use __init__ to abstract imports from underlying file hierarchy
# [TODO]: @brooke
from simplex import (
    SimplexPage, SIMUI, SimplexLayout
)
from simplex.view.simui.simui_select_item import SIMUISelectItem


data_view_bp = Blueprint('data_view', __name__)


@data_view_bp.route('/manage/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'POST':
        if 'data' not in request.files:
            flash('No file part')
        else:
            file = pd.read_csv(request.files.get('data'))
            # preserve headers
            col_options = file.columns
            col_options = (
                SIMUISelectItem()
                .set_select_options(col_options)
                .set_selected_option(col_options[0])
                .set_id(col_options[0])
                .render()
            )

            summary_header = '<h4 class="simplex-h4">Select Data Type:</h4>'
            file = DataSummary(file)
            summary_data = file.summarize()

            target_header = '<h4 class="simplex-h4">Select Target</h4>'
            target = col_options

            p1_header = (
                '<h4 class="simplex-h4">Select Prediction : Model 1</h4>')
            pred_one = col_options

            p2_header = (
                '<h4 class="simplex-h4">Select Prediction : Model 2</h4>')
            pred_two = col_options

            return render_template(
                'manage/data.html',
                summary=Markup(summary_data),
                target_header=Markup(target_header),
                target=Markup(target),
                p1_header=Markup(p1_header),
                pred_one=Markup(pred_one),
                p2_header=Markup(p2_header),
                pred_two=Markup(pred_two),
                summary_header=Markup(summary_header))

    return render_template('manage/data.html')
