# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This plugin provides support for specifying the -P option to test both
code and docs for a specific sub-package.
"""

import os
import pytest


def pytest_addoption(parser):

    parser.addoption("--package", "-P", action="store",
                     help="The name of a specific package to test, e.g. "
                          "'io.fits' or 'utils'. Accepts comma separated "
                          "string to specify multiple packages.")


@pytest.hookimpl(tryfirst=True)
def pytest_ignore_collect(path, config):

    # NOTE: it is important that when we don't want to skip a file we return
    # None and not False - if we return False pytest will not call any other
    # pytest_ignore_collect function in other plugins, e.g. pytest-doctestplus.

    # If the --package/-P option wasn't specified, don't do anything
    if config.getvalue('package') is None:
        return None

    # If the path is a directory, never skip - just do the filtering on a file
    # by file basis.
    if os.path.isdir(path):
        return None

    # Otherwise ignore filename for remainder of checks
    path = os.path.dirname(path)

    # Now convert the remainder of the path to subpackage name
    subpackage = '.'.join(path.split(os.path.sep))

    # Ignore any 'tests' directory
    if subpackage.endswith('.tests'):
        subpackage = subpackage[:-6]

    # Find selected sub-packages
    selected = config.getvalue('package').strip().split(',')

    # Finally, we check if this is one of the specified ones
    for subpackage_target in selected:
        if subpackage.endswith(subpackage_target):
            return None

    return True
