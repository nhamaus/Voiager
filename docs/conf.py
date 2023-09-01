# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pkg_resources import DistributionNotFound, get_distribution

try:
    ver = get_distribution("voiager").version
except DistributionNotFound:
    ver = "unknown"

project = 'Voiager'
copyright = '2023, Nico Hamaus'
author = 'Nico Hamaus'
release = ver

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx_rtd_size',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
#    'sphinx_automodapi.automodapi',
    ]

# Width of html pages
sphinx_rtd_size_width = "100%"

# Napoleon settings for docstrings
napoleon_google_docstring = True
napoleon_use_param = True
napoleon_use_rtype = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'voiager.png'
