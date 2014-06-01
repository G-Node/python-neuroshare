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
import os

#parse metadata from neuroshare/__init__.py
import re
srcdir = os.path.dirname(__file__)
path = os.path.join(srcdir, 'neuroshare', '__init__.py')
txt_data = open(path).read()
metadata = dict(re.findall("__([a-z]+)__ = [\"']([^\"']+)[\"']", txt_data))


classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: C',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules']

native_ext = Extension('neuroshare._capi',
                       include_dirs=[np.get_include()],
                       sources=['capi/nspy_glue.c'])

setup (name             = 'neuroshare',
       version          = metadata['version'],
       author           = metadata['author'],
       author_email     = metadata['contact'],
       url              = 'http://www.g-node.org/neuroshare-tools',
       keywords         = ['neuroshare', 'neuroscience', 'science'],
       description      = __doc__.split("\n")[0],
       long_description = "\n".join(__doc__.split("\n")[2:]),
       license          = 'LGPL',
       platforms        = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
       classifiers      = classifiers,
       ext_modules      = [native_ext],
       packages         = ['neuroshare'],
       scripts          = ['ns-convert'],
       setup_requires   = ['Sphinx-PyPI-upload', 'numpy >= 1.7']
       )
