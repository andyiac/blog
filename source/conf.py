import os
import sys



import sys
print(sys.path)


basedir = os.path.abspath(os.path.join('..', '..', 'kotlin-demo/source/'))


print("---------- base dir ----> " + basedir)

sys.path.insert(0, basedir)



# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'kotlin-demo'
copyright = '2024, findview'
author = 'findview'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx.ext.toctree',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


html_theme_options = {
    # 其他主题选项...
    'show_version': False,
    'show_sphinx': False,
    'show_related': False,
    'show_source': False,
    'navigation_depth': 3,
    'navigation_with_keys': True,
    'display_toc_level': 1,
}