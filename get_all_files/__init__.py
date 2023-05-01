import importlib.metadata
try:
    __version__ = importlib.metadata.version("get_all_files")
except:
    pass
from get_all_files._get_all_files import _get_all_files as get_all_files  # flake8: noqa