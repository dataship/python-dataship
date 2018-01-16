import os
import json
import numpy as np
import pandas as pd

EXTENSION_MAP = {
    ".i8" : "int8",
    ".u8" : "uint8",
    ".i16" : "int16",
    ".u16" : "uint16",
    ".i32" : "int32",
    ".u32" : "uint32",
    ".f32" : "float32",
    ".f64" : "float64"
}

reverse_extension_map = {value : key for key, value in EXTENSION_MAP.items()}

def load(root_dir, index):
    """Load data columns located at the given path using the given index.

    Args:
        root_dir: the path to the directory containing the data.
        index: a dictionary mapping column names to file names.

    Returns:
        a dictionary mapping column names to arrays of data
    """
    columns = {}

    # iterate through items in the index dictionary
    for column_name, file_name in index.items():
        # get extension
        basepath, ext = os.path.splitext(file_name)

        if(ext == ".json"):
            with open(root_dir + file_name, "rt") as json_file:
                columns[column_name] = json.loads(json_file.read())
        elif(ext in EXTENSION_MAP):
            dtype = EXTENSION_MAP[ext]
            with open(root_dir + file_name, 'rb') as binary_file:
                columns[column_name] = np.fromstring(binary_file.read(), dtype=dtype)

    return columns

def read(root_dir):
    """Look for an index in the specified directory and load it's data columns.
    Args:
        root_dir: the path to the directory containing the data columns and index.

    Returns:
        a dictionary mapping column names to arrays of data
    """
    with open(root_dir + "index.json", "rt") as f:
        index = json.loads(f.read())
        return load(root_dir, index)

def write(root_dir, columns, compact=True):
    """Write data columns to the given directory.
    Args:
        root_dir: the path to the directory to write the columns to
        columns: a dictionary mapping column names to column data

    column data should be a list of strings, or a numpy array
    """
    if(not root_dir[-1] == "/"): root_dir = root_dir + "/"

    index = {}

    for column_name, column_data in columns.items():
        if(type(column_data) == list and type(column_data[0]) == str):
            filename = column_name + ".json"
            with open(root_dir + filename, "wt") as f:
                if(compact):
                    f.write(json.dumps(column_data))
                else:
                    f.write(json.dumps(column_data, indent=1))
        elif(type(column_data) == np.ndarray):
            dtype = column_data.dtype.name
            if(dtype in reverse_extension_map):
                ext = reverse_extension_map[dtype]
            else:
                raise Exception("No mapping for dtype '" + dtype + "'")

            filename = column_name + ext
            with open(root_dir + filename, 'wb') as f:
                f.write(column_data.tostring())
        else:
            raise Exception("Unknown type for column '" + column_name +"': " + str(type(column_data)))

        index[column_name] = filename

    with open(root_dir + "index.json", 'wt') as f:
        if(compact):
            f.write(json.dumps(index))
        else:
            f.write(json.dumps(index, indent=1))

def dataframe(columns):
    """Turn a dictionary of columns into a Pandas dataframe.
    """

    column_dict = {}
    for column_name, data in columns.items():
        column_dict[column_name] = pd.Series(data)

    return pd.DataFrame(column_dict)
