# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mira3D User Manual'
copyright = '2023, Samisan Tech'
author = 'Samarth Tumdi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinxawesome_theme'
# html_theme = 'alabaster'
html_static_path = ['_static']

from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions

theme_options = ThemeOptions(
   # Add your theme options. For example:
   show_prev_next=True
)

html_theme_options = asdict(theme_options)
