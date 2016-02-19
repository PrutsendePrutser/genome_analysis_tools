# genome_analysis_tools/__init__.py

from flask import Flask
from blast_plus_tool import blast_plus_tool

# Create an app for this Python package
# Tell Flask to use the directory in which the init file is located as root, through __name__
app = Flask(__name__, instance_relative_config=True)

# Global config
app.config.from_object('config')

# Extend config with the sensitive info, from a different file
# instance_relative_config=True makes from_pyfile use the instance directory
# app.config.from_pyfile('config.py')

app.register_blueprint(blast_plus_tool, url_prefix='/blast_plus_tool')

# Only when executed from commandline or shell script, not if called from a test for example
if __name__ == '__main__':
    app.run()
