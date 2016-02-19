# genome_analysis_tools/utils/assets.py

"""Assets modules, used to bundle JS files, CSS files
"""

from flask.ext.assets import Bundle, Environment
from .. import app

bundles = {
    # Basic bundle that contains the required JS- and CSS-files
    'data_analysis_tools_js': Bundle(
        'js/lib/jquery_1.10.2.js',
        'js/lib/bootstrap.js',
        'js/main.js',
        output='gen/main.js'
    ),

    # Blast+ tool JS bundle
    'blast_plus_js': Bundle(
        'gen/main.js',
        'js/blast_plus.js',
        output='gen/blast_plus.js'
    ),

    # Blast+ tool CSS bundle
    'blast_plus_css': Bundle(
        'css/lib/bootstrap.css',
        'css/blast_plus.css',
        output='gen/blast_plus.css'
    )

}

assets = Environment(app)
assets.register(bundles)
