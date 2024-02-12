# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# Include root directory in path
sys.path.insert(0, os.path.abspath("../"))

# Find version
from pkg_resources import DistributionNotFound, get_distribution
try:
    ver = get_distribution("voiager").version
except DistributionNotFound:
    ver = "unknown"

project = 'Voiager'
copyright = '2024, Nico Hamaus'
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
#    'sphinxarg.ext',
    ]

# Modules to be mocked up for external dependencies that are not met at build time and break the building process.
autodoc_mock_imports = [
        'abel',
        'astropy',
        'cython',
        'emcee',
        'getdist',
        'h5py',
        'healpy',
        #'matplotlib',
        #'numpy',
        'pyabel',
        'pyyaml',
        'scipy',
        'tqdm',
        'vide',
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
#html_static_path = ['_static']
html_static_path = []
html_logo = 'voiager.png'
