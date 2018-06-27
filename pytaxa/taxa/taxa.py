from ..utils import *
from .taxon import Taxon

class Taxa(object):
    """
    Taxa class

    Stores one or more `taxon` objects. Prints first 10 taxa 
    for brevity sake.

    :param taxa: Any number of objects of type `Taxon` resulting from a call to
      :func:`~pytaxa.taxa.Taxon`

    Usage::
        
        # make a taxon
        from pytaxa import constructors as cs
        name = cs.taxon_name("Poa")
        rank = cs.taxon_rank("genus", "ncbi")
        db = cs.taxon_database("ncbi", 
            "http://www.ncbi.nlm.nih.gov/taxonomy",
            "NCBI Taxonomy Database", 
            "*")
        id = cs.taxon_id(12345, db)
        
        from pytaxa import Taxon
        tx = Taxon(name, rank, id, "L.")
        
        # combine many taxon's into taxa
        from pytaxa import Taxa
        Taxa(tx)
        bb = Taxa(tx, tx)
        bb

        # handles empty taxon objects
        Taxa(tx, Taxon(None), tx)

        # various accessors: len
        bb = Taxa(tx, tx)
        len(bb)
    """
    def __init__(self, *taxa: Taxon):
      super(Taxa, self).__init__()
      self.taxa = list(taxa)
      self.xlen = len(taxa)

    def __repr__(self):
      no = "<taxa>\n  no. taxa: %d\n  " % len(self.taxa)
      z = [self.print_taxon(z) for z in self.taxa[:10]]
      mssg = no + '\n  '.join(z)
      return mssg

    def __len__(self):
      return self.xlen

    @staticmethod
    def print_taxon(x):
      if all(b is None for b in x.name.values()): 
        return "empty"
      else:
        return ' / '.join([
          str(x.name.get('name')) or "", 
          str(x.rank.get('name')) or "",
          str(x.id.get('id')) or ""
        ])
