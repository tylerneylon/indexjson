""" make_data.py

    Usage:
        python3 make_data.py

    This script creates sample data files that are used by the unit tests.
    Since some data files are purposefully quite large, it's not great to check
    them into github or to make everyone download them. So, instead, only this
    script is checked in to the repo. It's deterministic, so everyone can still
    run the same tests on the same data.
"""


# ______________________________________________________________________
# Imports

import json
import random
import string


# ______________________________________________________________________
# Globals

used_keys = {''}  # The empty string is a sentinel value, always 'used'.


# ______________________________________________________________________
# Functions

# This creates a random json object.
# If `datatype` is provided, it should be either 'dict' or 'list' (as a
# string). The returned object may include lists, dicts, strings, and
# numbers. The maximum nesting depth is max_depth; eg, if max_depth is
# 1, then every list item (for lists) or every value (for dicts) is a
# leaf, which means a string or a number.
def make_json_obj(n, datatype=None, max_depth=1, max_str_len=10):
    if max_depth == 0:
        return make_leaf(max_str_len)
    if datatype is None:
        datatype = random.choice(['dict', 'list', 'leaf'])
    if datatype == 'dict':
        return {
            make_str(max_str_len):
                make_json_obj(
                    random.randint(1, 10),
                    max_depth=max_depth - 1
                )
            for _ in range(n)
        }
    if datatype == 'list':
        return [
            make_json_obj(random.randint(1, 10), max_depth=max_depth-1)
            for _ in range(n)
        ]
    if datatype == 'leaf':
        return make_leaf(max_str_len)

# Return, randomly, either a number (random) or a string (random, with length
# between 1 and max_str_len, inclusively).
def make_leaf(max_str_len):
    if random.choice(['str', 'num']) == 'num':
        return random.random()
    else:
        return make_str(max_str_len)

# Return a string with length in the interval [1, max_str_len].
# Each character is a random lowercase letter.
# This also ensures that each string returned is unique; this is useful for
# easily inserting random keys into a dict. If the strings were not unique, then
# there would be key overlap (randomly).
def make_str(max_str_len):

    global used_keys

    s = ''
    while s in used_keys:
        n = random.randint(1, max_str_len)
        s =  ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    used_keys.add(s)
    return s


# ______________________________________________________________________
# Main

if __name__ == '__main__':

    random.seed(42)

    list_obj = make_json_obj(100_000, 'list', max_depth=2)
    dict_obj = make_json_obj(100_000, 'dict', max_depth=2)

    with open('list.json', 'w') as f:
        json.dump(list_obj, f)
    with open('dict.json', 'w') as f:
        json.dump(dict_obj, f)
