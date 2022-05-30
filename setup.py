"""
Source Code from Keras EfficientDet implementation (https://github.com/xuannianz/EfficientDet) licensed under the Apache License, Version 2.0
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy

#setup function to compile the cython modules
from setuptools import find_packages

setup(
    name='efficientpose',
    version='1.0.0',
    description='EfficientPose',
    packages=find_packages(),
    ext_modules=cythonize("efficientpose/utils/compute_overlap.pyx"),
    include_dirs=[numpy.get_include()]
)
