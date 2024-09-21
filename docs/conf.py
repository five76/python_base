# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Основы Python'
copyright = '2024-2025'
author = 'qwe'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.imgconverter",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
#html_sidebars = {
#    "**": ["about.html", "searchbox.html", "localtoc.html", "navigation.html"]
#}
html_title = 'Сетевое и системное администрирование'
html_theme_options = {
    "prev_next_buttons_location": "both",
    "navigation_with_keys": True,
    "top_of_page_button": None,
    
    "light_css_variables": {
        "color-brand-primary": "#336790",  # "blue"
        "color-brand-content": "#336790",
    },
    "dark_css_variables": {
        "color-brand-primary": "#E5B62F",  # "yellow"
        "color-brand-content": "#E5B62F",
    },
}




#"announcement": (
#        'Книга не обновляется! Используется версия Ansible 2.9. '
#        '<a href="https://www.youtube.com/playlist?list=PLah0HUih_ZRnuI_K5-GV4FdAO9dVkRIGF">По некоторым темам есть видео лекции.</a>'
#    ),

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------


latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\documentclass[a4paper]{article}
\usepackage[12pt]{extsizes}
\usepackage[margin=1.0in]{geometry}
\usepackage{polyglossia}
\setcounter{secnumdepth}{0}
\setdefaultlanguage{russian}
\setotherlanguage{english}
\usepackage{fontspec}
\defaultfontfeatures{Scale=MatchLowercase}
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\setcounter{tocdepth}{2}
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    'figure_align': 'H',
}
