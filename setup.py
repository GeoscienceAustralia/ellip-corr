import os
from setuptools import setup
from setuptools.command.test import test as TestCommand

__version__ = "0.0.1"

ELLIP_CORR = os.path.dirname(__file__)


class PyTest(TestCommand, object):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        super(PyTest, self).initialize_options()
        self.pytest_args = []

    def finalize_options(self):
        super(PyTest, self).finalize_options()
        self.test_suite = True
        self.test_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        exit(pytest.main(self.pytest_args))


setup(
    name='ellip-corr',
    version=__version__,
    packages=['ellip', 'tau'],
    package_dir={'ellip-corr': 'ellip'},
    include_package_data=True,
    entry_points={},
    setup_requires=['numpy'],
    install_requires=['numpy', 'cython'],
    extras_require={
        'dev': [
            'pytest >= 3.2.0',
        ]
    },
    tests_require=[
        'pytest',
    ],
    license="See Readme",
    zip_safe=False,
    keywords='ak135, travel time, iasp91, ellipticity correction, obspy',
    classifiers=[
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        # add additional supported python versions
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis"
        # add more topics
    ],
    cmdclass={
        'test': PyTest,
    }
)

# Build the f2py fortran extension
# --------------------------------
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

ellipcorr = Extension(
    name='ellipcorr',
    # add several modules files under the same extension
    sources=['ellip/ellipcorr.f']
)

setup(
    name='ellipcorr',
    ext_modules=[ellipcorr]
    )
