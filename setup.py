import setuptools

def setup_for_python36():
    from setuptools_movandi import ppsetuptools
    from setuptools_movandi.dependency_parser import parse_requirements
    from setuptools_movandi.version_schemer import version_scheme
    import os
    rootdir = os.getcwd()
    ppsetuptools.setup(
        install_requires = parse_requirements(rootdir, os.path.join(rootdir,'requirements.txt')),
        # use_scm_version={
        #     "git_describe_command": 'git describe --tags --long --match "v*"',
        #     "version_scheme": version_scheme,
        #     "local_scheme": "no-local-version",
        #     "relative_to": __file__,
        #     "write_to": f"{rootdir}/src/sample/_version.py",
        # },
    )

if setuptools.__version__ >= '61':
    setuptools.setup()
else:
    setup_for_python36()
