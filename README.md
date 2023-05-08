# READ ME

![tests](https://github.com/bwheelz36/get_all_files/actions/workflows/run_tests.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/get_all_files.svg)](https://badge.fury.io/py/get_all_files)
[![codecov](https://codecov.io/gh/bwheelz36/get_all_files/branch/main/graph/badge.svg?token=CCVB5BAR8W)](https://codecov.io/gh/bwheelz36/get_all_files)


This is a very simple package which is basically a wrapper around glob; it simply gets all the files with extension matching a list of extensions in a given
directory. I found that I was including functionality like this in so many other projects I might as well just make
it a package. Plus I wanted to play with poetry. 

## install 

```bash
pip install get_all_files
```

## Examples

**get all jpg files in home directory**
```python
from get_all_files import get_all_files
from pathlib import Path

home_dir = Path('~').expanduser()
jpg_files = get_all_files(home_dir, 'jpg')
```

**get all jpg AND png files in home directory**
```python
from get_all_files import get_all_files
from pathlib import Path

home_dir = Path('~').expanduser()
jpg_files = get_all_files(home_dir, ['jpg', 'png'])
```

**get all jpg files starting with 'a' in home directory**
```python
from get_all_files import get_all_files
from pathlib import Path

home_dir = Path('~').expanduser()
jpg_files = get_all_files(home_dir, 'jpg', file_name='a*')
```

**get absolute file paths instead of file names**
```python
from get_all_files import get_all_files
from pathlib import Path

home_dir = Path('~').expanduser()
jpg_files = get_all_files(home_dir, ['jpg', 'png'], return_absolute_filepath=True)
```

**Loop over multiple directories**

This package is not recursive - if you want to process multiple directories you have to do it yourself:

```python
from get_all_files import get_all_files
from pathlib import Path
import os

home_dir = Path('~').expanduser()
subfolders = [f.path for f in os.scandir(home_dir) if f.is_dir()]
extension = 'txt'  # why not
all_files = []
for folder in subfolders:
    files = get_all_files(folder, extension, return_absolute_filepath=True)
    all_files.extend(files)
```
