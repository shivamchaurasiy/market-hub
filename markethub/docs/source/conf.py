# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'markethub'
copyright = '2024, shivamchaurasiya'
author = 'shivamchaurasiya'
release = '28/10/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'english'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os

# Get the current version from Read the Docs environment, fallback to "main" if not found
project_version = os.getenv("READTHEDOCS_VERSION", "main")

# Set up the HTML context for Sphinx, so it can display the version
html_context = {
    "display_version": project_version,
}
