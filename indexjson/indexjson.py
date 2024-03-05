""" indexjson.py

    Usage:

        import indexjson

        # The first load of a json file will automatically index it. Later load
        # calls will automatically use the pre-made index. The index file will
        # be updated automatically if the underlying file changes.

        with open('myfile.json') as f:
            data = indexjson.load(f)
"""


# ______________________________________________________________________
# To-do items
#
# * [ ] Use a faster json library under the hood, such as simdjson.


# ______________________________________________________________________
# Imports

import json


# ______________________________________________________________________
# Public interface

def load(fp):
    index_path = _get_index_path(fp)  # NOTE: Use f.name to help.
    if not _index_is_current(fp, index_path):
        return _make_index(fp, index_path)
    else:
        return _load_index(index_path)


# ______________________________________________________________________
# Internal functions

# This returns the index file for `fp` as a Path object.
# This does _not_ check if the path exists.
def _get_index_path(fp):
    pass

# This returns True iff the index_path exists, and has an mtime >= the mtime of
# the source file fp.
def _index_is_current(fp, index_path):
    pass

# This creates the index file for source file `fp`, and returns the
# resulting index view.
def _make_index(fp, index_path):
    pass

# This loads and returns the index view stored at the given index_path.
def _load_index(index_path):
    pass


# ______________________________________________________________________
# Internal classes

class _IndexView(object):
    def __init__(self):
        pass  # Init things like self.whatever = 3
