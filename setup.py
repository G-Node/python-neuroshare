#!/usr/bin/env python
"""Python Bindings for Neuroshare
---------------------------------

The Neuroshare API is a standardized interface to access
electrophysiology data stored in various different file
formats. To do so, it uses format- specific shared libraries.
Refer to the official website
     		    http://neuroshare.org
for more information.

The aim of this library is to provide a high level interface
to the Neuroshare API, i.e. it focuses on API usability more
then being a mere python version of the C API. Thus none of
the original Neuroshare API calls are directly exposed but
the interface is through python objects that resemble (more
or less) the Neuroshare Entities.
"""

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
    from distutils.extension import Extension

import numpy as np

classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: C',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules']

native_ext = Extension('neuroshare._capi',
                       include_dirs = [np.get_include()],
                       sources = ['capi/nspy_glue.c'])

setup (name             = 'neuroshare',
       version          = '0.8.8',
       author           = 'Christian Kellner',
       author_email     = 'kellner@biologie.uni-muenchen.de',
       url              = 'http://www.g-node.org/neuroshare-tools',
       keywords         = ['neuroshare'],
       description      = __doc__.split("\n")[0],
       long_description = "\n".join(__doc__.split("\n")[2:]),
       classifiers      = classifiers,
       ext_modules      = [native_ext],
       packages         = ['neuroshare'],
       scripts          = ['ns-convert'],
       setup_requires   = ['sphinx', 'Sphinx-PyPI-upload']
       )
