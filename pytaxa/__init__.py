# -*- coding: utf-8 -*-

# pytaxa

'''
pytaxa library
~~~~~~~~~~~~~~~~~~~~~

pytaxa provides taxonomic classes.

Usage::

   # setup a different base URL
   from pytaxa import Taxa
   x = Taxa()
   x.taxon_name("Poa")
   x.taxon_name("undefined")
   x.taxon_name("species 1")
   x.taxon_name("Poa annua")
   x.taxon_name("Poa annua L.")
'''

__title__ = 'pytaxa'
__version__ = '0.0.1.9100'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .taxa import Taxa
