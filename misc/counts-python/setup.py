from distutils.core import setup
from Cython.Build import cythonize

setup(name="counts", ext_modules=cythonize('counts.pyx'),)
