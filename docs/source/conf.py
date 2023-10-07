# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Computerprogrammeren voor het pregymnasium'
copyright = '2023, S. Faas'
author = 'S. Faas'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_exercise',
              'sphinx_togglebutton']

templates_path = ['_templates']
exclude_patterns = ['.venv']

language = 'nl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for togglebutton extension:
togglebutton_hint = "Inhoud tonen"
togglebutton_hint_hide = "Inhoud verbergen"