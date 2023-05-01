from pathlib import Path
import glob
import os
import warnings


def _process_input_path(path_to_data: (Path, str)) -> Path:
    """
    internal function to pre-process and check the input path
    """
    if isinstance(path_to_data, str):
        path_to_data = Path(path_to_data)
    if not isinstance(path_to_data, Path):
        raise TypeError(f'path_to_data must be type Path or str, not {type(path_to_data)}')
    if not path_to_data.is_dir():
        raise NotADirectoryError(f'invalid path supplied; {path_to_data} does not exist')
    return path_to_data


def _process_extensions(file_extensions: (str, list)) -> list:
    """
    internal function to pre-process and check input file extensions
    :param file_extensions:
    :return:
    """
    if isinstance(file_extensions, str):
        file_extensions = [file_extensions]
    if not isinstance(file_extensions, list):
        raise TypeError(f'file_extensions must be type str or list, not {type(file_extensions)}')
    processed_extensions = []
    for extension in file_extensions:
        if not file_extensions[0] == '.':
            # handles the case where the user entered 'jpg' instead of '.jpg'
            extension = '.' + extension
        # add wildcard
        extension = '*' + extension
        # verify that this is now in the format we require
        if not extension[0:2] == '*.':
            # don't think it's possible to get here but just in case
            raise Exception('please enter the file_extensions parameter like this : file_extensions = "jpg"')
        processed_extensions.append(extension)
    return processed_extensions


def _get_all_files(path_to_data: (Path, str), file_extensions: (str, list),
                   return_absolute_filepath: bool = False) -> list:
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
    path_to_data = _process_input_path(path_to_data)

    # process extensions:
    file_extensions = _process_extensions(file_extensions)

    Files = []
    for extension in file_extensions:
        # find the files matching this extension
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
