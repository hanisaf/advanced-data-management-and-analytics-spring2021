# Docutils

## Presentation

Click [here](https://youtu.be/fe2TAYIYT5o) for the video presentation

## Summary of Support Files

- `demo.ipynb`: the notebook containing the tutorial code
- `Docutils.zip`: the zip folder containing out files converted from plaintext to XML, HTML formats

## Installation Instructions

Use `!pip install docutils` to install the `docutils` package. Next, use `import docutils`to import the package into your notebook.

For example, to import specific modules from `docutils` package use the following line of code:
 `from docutils import core, io`
 

## Guide

### __docutils 0.17.1 version__

- Author: David Goodger
- Contact: goodger@python.org

[Docutils](https://pypi.org/project/docutils/) is an open-source, modular text processing system for processing plaintext documentation into a more useful format. Formats include HTML, man-pages, OpenDocument, LaTeX, or XML.

Docutils supports reStructuredText for input, an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.

Docutils is short for "Python Documentation Utilities".

Support for the following sources has been implemented:
 - Standalone files
 - `PEPs (Python Enhancement Proposals)`
 
Support for these sources is currently being developed:
 - Inline documentation
 - Wikis
 - Email and more

Docutils Distribution Consists of:
 - the `docutils` package (or library)
 - front-end tools
 - test suite
 - documentation.
 

## Notable docutils Modules & Subpackages
-----------------------------
Module        | Definition
------------- | -------------
__core__      | Contains the ``Publisher`` class and ``publish_()``convenience functions
__io__        | Provides a uniform API for low-level input and output
__nodes__     | Docutils document tree (doctree) node class library


-----------------------------
Subpackages   | Definition
------------- | -------------
**languages** | Language-specific mappings of terms
**parsers**   | Syntax-specific input parser modules or packages
**readers**   | Context-specific input handlers which understand the data source and manage a parser


### __Below is an overview of the `docutils` package:__
![alt text](docutils.png "Docutils")


## Main Use Applications of Package

The reStructured Text component of the `docutils` package makes it easy to convert between different formats, especially from plain text to a static website. It is unique because it is extensible. Better than simpler markups. 

Additionally, users can pair `docutils` with `Sphinx` to convert text to html. The `Sphinx` package is built on the `docutils` package. The docutils parser creates the parse tree as a representation of the text in the memory for the Sphinx application and .rst environment.

Docutils provides programmers with a set of tools to process plaintext documentation into various formats. Examples of this can be seen in converting text to website formats.
