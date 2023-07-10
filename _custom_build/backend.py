from setuptools import build_meta as _orig
from setuptools.build_meta import *

def git_submodules_as_deps():
    # TODO: actual logic
    # return [ "libcalc==0.0.1" ]
    return [ "pandas" ]

# def build_sdist(self, sdist_directory, config_settings=None):
#     # return self._build_with_temp_dir(
#     #     ['sdist', '--formats', 'gztar'], '.tar.gz', sdist_directory, config_settings
#     # )
#     print(f" ============================= build_sdist ")
#     return "FLKJ"

def build_wheel(
    wheel_directory, config_settings=None, metadata_directory=None
):
    return "FLKJ"

def prepare_metadata_for_build_wheel(
    metadata_directory, config_settings=None
):
    print(f" ============================= prepare_metadata_for_build_wheel")
    return "FLKJ"
