import setuptools

def setup_for_python36():
    import setuptools_movandi
    from setuptools_movandi import parse_dependencies, parse_requirements
    import os
    cwd = os.getcwd()
    setuptools_movandi.setup(
        install_requires = parse_requirements(os.path.join(cwd,'requirements.txt')),
    )

if setuptools.__version__ >= '61':
    setuptools.setup()
else:
    setup_for_python36()
