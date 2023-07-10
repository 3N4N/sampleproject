from pathlib import Path
from setuptools.dist import Distribution

def use_pipfile(dist, attr, value):
    print(f" ============================= use_pipfile_")
    if not value:
        return


def finalize_dist(Distribution):
    print(f" ============================= finalize_dist_")
