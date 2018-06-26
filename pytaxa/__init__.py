# -*- coding: utf-8 -*-

# pytaxa

'''
pytaxa library
~~~~~~~~~~~~~~~~~~~~~

pytaxa provides taxonomic classes.

Usage::

   from pytaxa import Taxa
   x = Taxa()
   x.taxon_name("Poa")
   x.taxon_name("undefined")
   x.taxon_name("species 1")
   x.taxon_name("Poa annua")
   x.taxon_name("Poa annua L.")
'''

__title__ = 'pytaxa'
__version__ = '0.0.1.4'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .constructors import taxon_name, taxon_database, taxon_id, taxon_rank
from .taxa import Taxon, Taxa, Hierarchy, Hierarchies
from .examples import eg_hierarchy
