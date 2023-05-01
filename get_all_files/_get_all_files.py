from pathlib import Path
import glob
import os
import warnings

def get_all_files(path_to_data: (Path, str), file_extensions: (str, list),
                  return_absolute_filepath: bool = False):
    """
    quick script to just collect all the files in the Analysis path

    :param path_to_data: folder where the files are
    :type path_to_data: pathlib.Path, string
    :param file_extensions: extension of files to return, e.g. 'dcm'
    :type file_extensions: str, list
    :param return_absolute_filepath: if False (default) file names are returned; if True absolute file names returned
    :returns Files: list of all found files
    """
    # process input path:
    if isinstance(path_to_data, str):
        path_to_data = Path(path_to_data)
    if not isinstance(path_to_data, Path):
        raise TypeError(f'path_to_data must be type Path or str, not {type(path_to_data)}')
    if not path_to_data.is_dir():
        raise NotADirectoryError(f'invalid path supplied; {path_to_data} does not exist')

    # process extensions:
    if isinstance(file_extensions, str):
        file_extensions = [file_extensions]
    if not isinstance(file_extensions, list):
        raise TypeError(f'file_extensions must be type str or list, not {type(file_extensions)}')

    Files = []
    for extension in file_extensions:
        if not file_extensions[0] == '.':
            # handles the case where the user entered 'jpg' instead of '.jpg'
            extension = '.' + extension
        # add wildcard
        extension = '*' + extension
        # verify that this is now in the format we require
        if not extension[0:2] == '*.':
            raise Exception('please enter the file_extensions parameter like this : file_extensions = "jpg"')
        # now find the files matching this extension
        AllFiles = glob.glob(str(path_to_data / extension))
        # process all found files into desired format
        for file in AllFiles:
            if return_absolute_filepath:
                Files.append(file)
            else:
                head, tail = os.path.split(file)
                Files.append(tail)

        if not Files:
            warnings.warn(f'no {extension} files in {path_to_data}')

    return Files
