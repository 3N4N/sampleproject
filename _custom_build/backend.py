from setuptools import build_meta as _orig
from setuptools.build_meta import *

def git_submodules_as_deps():
    # TODO: actual logic
    # return [ "libcalc==0.0.1" ]
    return [ "pandas" ]

def get_requires_for_build_wheel(config_settings=None):
    return _orig.get_requires_for_build_wheel(config_settings) + git_submodules_as_deps()

def get_requires_for_build_sdist(config_settings=None):
    return _orig.get_requires_for_build_sdist(config_settings) + git_submodules_as_deps()
