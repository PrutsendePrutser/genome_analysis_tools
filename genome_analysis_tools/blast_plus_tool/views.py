from . import blast_plus_tool
from flask import render_template


@blast_plus_tool.route('/')
def blast_plus_index():
    return render_template('blast_plus_tool/data_analysis.html')
