from ..utils import *
from typing import Union
from ..constructors import *

class Taxon(object):
    """
    Taxon class

    Create a `taxon` object

    :param name: A dict resulting from a call to :func:`~pytaxa.constructors.taxon_name`
      with `name` and `database` keys, or a name as a `str`
    :param rank: A dict resulting from a call to :func:`~pytaxa.constructors.taxon_rank`
      with `name` and `database` keys, or a name as a `str`
    :param id: A dict resulting from a call to :func:`~pytaxa.constructors.taxon_id`
      with `id` and `database` keys, or an identifier as an `int`
    :param authority: An authority name as a `str`

    Usage::
        
        from pytaxa import constructors as cs
        from pytaxa import Taxon
        name = cs.taxon_name("Poa")
        rank = cs.taxon_rank("genus", "ncbi")
        db = cs.taxon_database("ncbi", 
            "http://www.ncbi.nlm.nih.gov/taxonomy",
            "NCBI Taxonomy Database", 
            "*")
        id = cs.taxon_id(12345, db)
        x = Taxon(name, rank, id, "L.")
        x.is_empty()

        # null taxon's
        x = Taxon(None)
        x
        x.is_empty()
        Taxon({})
        Taxon(None, None, None)
        Taxon(None, None, id)
        Taxon(None, None, None, "L.")
    """
    def __init__(self, 
      name: Union[str,dict] = {}, 
      rank: Union[str,dict] = {}, 
      id: Union[str,dict] = {}, 
      authority: str = ''):

      super(Taxon, self).__init__()
      self.name = name if isinstance(name, dict) else taxon_name(name) if isinstance(name, str) else {}
      self.rank = rank if isinstance(rank, dict) else taxon_rank(rank) if isinstance(rank, str) else {}
      self.id = id if isinstance(id, dict) else taxon_id(id) if isinstance(id, str) else {}
      self.authority = authority

    def __repr__(self):
      tx = "<Taxon>\n  "
      txt = [
        'name: ' + str(self.name.get('name')) or "", 
        'rank: ' + str(self.rank.get('name')) or "",
        'id: ' + str(self.id.get('id')) or "",
        'authority: ' + self.authority or ""
      ]
      mssg = tx + '\n  '.join(txt)
      return mssg

    def print_taxon(self):
      if all(b is None for b in self.name.values()): 
        return "empty"
      else:
        return ' / '.join([
          str(self.name.get('name')) or "", 
          str(self.rank.get('name')) or "",
          str(self.id.get('id')) or ""
        ])
    
    def is_empty(self):
      return not self.name and not self.rank and not self.id
