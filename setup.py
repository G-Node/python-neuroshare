#!/usr/bin/env python
"""Neuroshare Bindings for Python

"""

from distutils.core import setup, Extension
import setuptools
from distutils.extension import Extension
import numpy as np

classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: C',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Intended Audience :: Developers']

native_ext = Extension('neuroshare._capi',
                       include_dirs = [np.get_include()],
                       sources = ['capi/nspy_glue.c'])

setup (name             = 'neuroshare',
       version          = '0.8',
       author           = 'Christian Kellner',
       author_email     = 'kellner@biologie.uni-muenchen.de',
       description      = __doc__.split("\n")[0],
       long_description = "\n".join(__doc__.split("\n")[2:]),
       classifiers      = classifiers,
       ext_modules      = [native_ext],
       packages         = ['neuroshare']
       )
