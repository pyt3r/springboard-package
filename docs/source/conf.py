# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import sys
import pathlib
from io import open
import yaml
import sphinx_rtd_theme
here = pathlib.Path(__file__).resolve().parent
pkg  = here / '..' / '..'
sys.path.insert( 0, str( pkg ))
meta = yaml.safe_load( open( pkg/ 'conda-recipe' / 'meta.yaml', 'rb' ))


# -- Master document --------------------------------------------------------------
master_doc = 'index'


# -- Project information -----------------------------------------------------
author = meta['about']['author']
project = meta['package']['name']
copyright = f'2025, {author}'
release = str(meta['package']['version'])


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.napoleon',
    #'sphinx.ext.intersphinx',
    'rst2pdf.pdfbuilder',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


_example_dir  = pathlib.Path( '..' ) / 'assignments'
_example_dirs = [ d for d in _example_dir.iterdir() if d.is_dir() ]
_gallery_dirs = [ d.name for d in _example_dirs ] 

# sphinx-gallery configuration
sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': _example_dirs,
    # path to where to save gallery generated output
    'gallery_dirs': _gallery_dirs,
    # specify that examples should be ordered according to filename
    #'within_subsection_order': FileNameSortKey,
    # directory where function granular galleries are stored
    #'backreferences_dir': 'gen_modules/backreferences',
    # Modules for which function level galleries are created.
    'doc_module': (project),
    # include all files in the examples_dirs, except __init__.py
    'filename_pattern': '/',
    'ignore_pattern': '__init__\\.py',
}


# -- Options for PDF output -------------------------------------------------s
pdf_documents = [('index', project, project+release, author)]
