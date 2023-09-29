# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import date


# -- General configuration ---------------------------------------------------

copyright = f"{date.today().year}"

extensions = ['myst_parser',
              "sphinx_design",
              'nbsphinx',
              'sphinxcontrib.email',
              ]


# -- Options for MyST -------------------------------------------------

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
myst_title_to_header = False
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
email_automode = True
master_doc = "index"
html_theme = 'alabaster'
html_static_path = ['static_free']
latex_engine = 'xelatex'
myst_words_per_minute = 30
