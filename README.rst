========================
pytest-filter-subpackage
========================

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10779130.svg
    :target: https://doi.org/10.5281/zenodo.10779130
    :alt: 10.5281/zenodo.10779130

.. image:: https://github.com/astropy/pytest-filter-subpackage/actions/workflows/python-tests.yml/badge.svg?branch=main
    :target: https://github.com/astropy/pytest-filter-subpackage/actions/workflows/python-tests.yml
    :alt: CI

This package contains a simple plugin for the `pytest`_ framework that provides a
shortcut to testing all code and documentation for a given sub-package.

.. _pytest: https://pytest.org/en/latest/

Installation
------------

The ``pytest-filter-subpackage`` plugin can be installed using ``pip``::

    $ pip install pytest-filter-subpackage

It is also possible to install the latest development version from the source
repository::

    $ git clone https://github.com/astropy/pytest-filter-subpackage
    $ cd pytest-filter-subpackage
    $ pip install .

In either case, the plugin will automatically be registered for use with
``pytest``.

Usage
-----

This plugin provides a ``-P`` option which takes a comma-separated list
of sub-package names (without the top-level package name)::

    pytest -P wcs,io.fits

which is equivalent to::

    pytest **/wcs **/io/fits

When used in conjunction with `pytest-doctestplus
<http://github.com/astropy/pytest-doctestplus>`_ this will result in both
the narrative documentation and code being tested for a given sub-package.

License
-------
This plugin is licensed under a 3-clause BSD style license - see the
``LICENSE.rst`` file.
