# -*- coding: utf-8 -*-

# pytaxa

'''
pytaxa library
~~~~~~~~~~~~~~~~~~~~~

pytaxa provides taxonomic classes.

Usage::

    # constructors
    from pytaxa import constructors as cs
    cs.taxon_name("Poa")
    
    # Taxon
    from pytaxa import Taxon
    x = Taxon(None)
    x.is_empty()

    # Taxa
    name = cs.taxon_name("Poa")
    rank = cs.taxon_rank("genus", "ncbi")
    db = cs.taxon_database("ncbi", 
      "http://www.ncbi.nlm.nih.gov/taxonomy",
      "NCBI Taxonomy Database", 
      "*")
    id = cs.taxon_id(12345, db)
    tx1 = Taxon(name, rank, id, "L.")
    tx2 = Taxon(cs.taxon_name("Poaceae"), 
      cs.taxon_rank("family", "ncbi"), cs.taxon_id(4479, db))
    tx3 = Taxon(cs.taxon_name("Poa annua"), 
      cs.taxon_rank("species", "ncbi"), cs.taxon_id(93036, db))
    from pytaxa import Taxa
    Taxa(tx1, tx2, tx3)

    # Hierarchy
    from pytaxa import Hierarchy
    out = Hierarchy(tx1, tx2, tx)
    out.taxa
    out.ranklist
    out.all_empty()
    out.pop(ranks = "family")
'''

__title__ = 'pytaxa'
__version__ = '0.0.7'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .constructors import taxon_name, taxon_database, taxon_id, taxon_rank
from .taxa import Taxon, Taxa, Hierarchy, Hierarchies
from .examples import eg_hierarchy
