from ..utils import *

class Taxa(object):
    """
    Taxa class

    Stores one or more `taxon` objects. Prints first 10 taxa 
    for brevity sake.

    Usage:::
        
        # make a taxon
        from pytaxa import constructors as cs
        name = cs.taxon_name("Poa")
        rank = cs.taxon_rank("genus", "ncbi")
        db = cs.taxon_database("ncbi", 
            "http://www.ncbi.nlm.nih.gov/taxonomy",
            "NCBI Taxonomy Database", 
            "*")
        id = cs.taxon_id(12345, db)
        tx = cs.taxon(name, rank, id, "L.")
        
        # combine many taxon's into taxa
        from pytaxa import Taxa
        Taxa(tx)
        bb = Taxa(tx, tx)

        # handles empty taxon objects
        Taxa(tx, cs.taxon(None), tx)

        # various accessors: len
        bb = Taxa(tx, tx)
        len(bb)
    """
    def __init__(self, *x):
      super(Taxa, self).__init__()
      self.x = x
      self.xlen = len(x)

    def __repr__(self):
      no = "<taxa>\n  no. taxa: %d\n  " % len(self.x)
      z = [self.print_taxon(z) for z in self.x[:10]]
      mssg = no + '\n  '.join(z)
      return mssg

    def __len__(self):
      return self.xlen

    @staticmethod
    def print_taxon(x):
      if all(b is None for b in x.values()): 
        return "empty"
      else:
        return ' / '.join([
          gt(x['name'], 'name', ""), 
          gt(x['rank'], 'name', ""),
          str(gt(x['id'], 'id', ""))
        ])

