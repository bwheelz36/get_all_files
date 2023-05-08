"""
tests for get_all_files
"""

from pathlib import Path
import sys
import os
import pytest
this_file_loc = Path(__file__).parent
sys.path.insert(0, str(this_file_loc.parent))
from get_all_files import get_all_files  # flake8: noqa


def test_single_extension_use():
    home_dir = Path('~').expanduser()
    extension = 'random_extension'
    file_to_write = home_dir / ('arbitrary_file.' + extension)
    with open(file_to_write, 'w') as f:
        f.write('ooga booga!')

    files = get_all_files(home_dir, extension)
    assert files[0] == file_to_write.name


def test_remultiple_extension_use():
    home_dir = Path('~').expanduser()
    extension1 = 'random_extension1'
    extension2 = 'random_extension2'
    file_to_write1 = home_dir / ('arbitrary_file.' + extension1)
    file_to_write2 = home_dir / ('arbitrary_file.' + extension2)
    with open(file_to_write1, 'w') as f:
        f.write('ooga booga!')
    with open(file_to_write2, 'w') as f:
        f.write('ooga booga!')
    files = get_all_files(home_dir, [extension1, extension2])
    for file in files:
        assert file.split('.')[1] in [extension1, extension2]


def test_absolute_path_use():
    home_dir = Path('~').expanduser()
    extension1 = 'random_extension1'
    extension2 = 'random_extension2'
    file_to_write1 = home_dir / ('arbitrary_file.' + extension1)
    file_to_write2 = home_dir / ('arbitrary_file.' + extension2)
    with open(file_to_write1, 'w') as f:
        f.write('ooga booga!')
    with open(file_to_write2, 'w') as f:
        f.write('ooga booga!')
    files = get_all_files(home_dir, [extension1, extension2], return_absolute_filepath=True)
    for file in files:
        assert Path(file).parent == home_dir
        assert Path(file).name.split('.')[1] in [extension1, extension2]


def test_with_subfolders():
    """
    this is more a test that this runs than aa test of functinoality
    :return:
    """

    home_dir = Path('~').expanduser()
    subfolders = [f.path for f in os.scandir(home_dir) if f.is_dir()]
    extension = 'txt'  # why not
    all_files = []
    for folder in subfolders:
        files = get_all_files(folder, extension, return_absolute_filepath=True)
        all_files.extend(files)


def test_passing_non_existent_directory():
    home_dir = Path('~').expanduser()
    not_a_directory = home_dir / 'this_directory_better_not_exist_afgaergaeg'
    assert not not_a_directory.is_dir()
    with pytest.raises(NotADirectoryError):
        # this asserts that a NotADirectoryError is being raised
        get_all_files(not_a_directory, 'bla')

    with pytest.raises(TypeError):
        get_all_files([not_a_directory], 'bla')


def test_passing_extensions_with_different_formats():
    home_dir = Path('~').expanduser()

    with pytest.raises(TypeError):
        get_all_files(home_dir, 123)


def test_filename_wildcards():
    home_dir = Path('~').expanduser()
    extension1 = 'random_extension1'
    file_to_write1 = home_dir / ('arbitrary_file.' + extension1)
    file_to_write2 = home_dir / ('garbitrary_file.' + extension1)  # this shouldn't get picked up
    with open(file_to_write1, 'w') as f:
        f.write('ooga booga!')
    with open(file_to_write2, 'w') as f:
        f.write('ooga booga!')
    files = get_all_files(home_dir, extension1, file_name='a*', return_absolute_filepath=True)
    for file in files:
        assert Path(file).parent == home_dir
        assert Path(file).name.split('.')[1] in [extension1]
        assert Path(file).name == 'arbitrary_file.' + extension1
