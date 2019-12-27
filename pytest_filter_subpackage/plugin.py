# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This plugin provides support for specifying the -P option to test both
code and docs for a specific sub-package.
"""

import os


def pytest_addoption(parser):

    parser.addoption("--package", "-P", action="store",
                     help="The name of a specific package to test, e.g. "
                          "'io.fits' or 'utils'. Accepts comma separated "
                          "string to specify multiple packages.")


def pytest_ignore_collect(path, config):

    # If the --package/-P option wasn't specified, don't do anything
    if config.getvalue('package') is None:
        return False

    # Convert the path to the file being checked to a relative path.
    path = os.path.relpath(path, os.path.curdir)

    # If the path is a directory, never skip - just do the filtering on a file
    # by file basis.
    if os.path.isdir(path):
        return False

    # We split the path up and ignore the first part of the path, which could
    # be the main package name, or e.g. 'docs'.
    split_path = path.split(os.path.sep)[1:]

    # Now convert the remainder of the path to subpackage name
    subpackage = '.'.join(split_path)

    # Finally, we check if this is one of the specified ones
    for subpackage_target in config.getvalue('package').split(','):
        if subpackage.startswith(subpackage_target):
            return False

    return True
