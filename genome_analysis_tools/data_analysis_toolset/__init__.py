# genome_analysis_tools/data_analysis_toolset/__init__.py

from flask import Blueprint

# The line below imports the BlastPlusTool model class, from the models.py module one directory up

# from ..models import BlastPlusTool

# Create the blueprint, using this directory as root for the app
blast_plus_tool = Blueprint('data_analysis_tools', __name__, template_folder='templates', static_folder='static')


# The lines below need to be used when we store BlastPlusTool stuff in the database
# This will retrieve the correct data depending on the combination of requested URL and user
# @blast_plus_tool.url_value_preprocessor
# def get_site(endpoint, values):
#    query = BlastPlusTool.query.filter_by(subdomain=values.pop('site_subdomain'))
#    g.site = query.first_or_404()

# Import the views module from this package at the end, to avoid circular imports
# We need the blast_plus_tool variable in views, so doing it this way avoids problems with circular imports
import views
