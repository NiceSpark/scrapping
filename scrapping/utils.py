"""This file contains helper functions for writing json documents, as well as creating timestamp (that you need for those json)"""

import json
import os
import time
from datetime import datetime


def open_json(filename):
    """
    open a .json file from the file path (filename)
    """
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        print(f"file {filename} does not exists !")
        return {}


def write_json(filename, json_file):
    """
    write a json_file to the file path (filename)
    """
    with open(filename, "w+") as f:
        json.dump(json_file, f, indent=4, default=str)

# function to ensure all key data fields have a value


def validate_field(field):  # if field is present pass if field:pass
    # if field is not present print text else:
    field = 'No results'
    return field


def validate_url(url):
    return ("linkedin.com" in url.text) and (url.text[-3:] != "...")
