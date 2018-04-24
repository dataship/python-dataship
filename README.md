# dataship

Lightweight tools for reading, writing and storing data, locally and over the internet.

Allows easy interaction with browser and node based data visualization and analysis tools.
Built on numpy and works with pandas.

# install
`pip install dataship`

# example

Write files locally like this,
```python
import numpy as np
from dataship import beam

names = ['eeny', 'meeny', 'miney', 'moe']
counts = np.array([1, 2, 3, 4], dtype="int8")

columns = {
    "name" : names,
    "count" : counts
}

beam.write("./toeses", columns)
```

Read that into pandas like this,
```python
columns = beam.read("./toeses")
frame = beam.to_dataframe(columns) # Dataframe
```

The variable `frame` now contains a pandas Dataframe that looks like this:

name | count
-----|-------
eeny | 1
meeny | 2
miney | 3
moe | 4


and the directory `./toeses` contains these files:

```shell
index.json # special file describing columns (json)
name.json # data for name column (json)
count.i8 # data for count column (binary)
```

data files can be viewed with [arrayviewer](https://github.com/waylonflinn/arrayviewer)


You can also serialize an existing Pandas Dataframe like this,
```python
columns = beam.from_dataframe(frame)
beam.write("./toeses", columns)
```
