from ..utils import *
from typing import Union
from ..constructors import *

class Taxon(object):
    """
    Taxon class

    Create a `taxon` object

    Usage:::
        
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
      mssg = self.print_taxon()
      return mssg

    def print_taxon(self):
      tx = "<Taxon>\n  "
      txt = [
        'name: ' + str(self.name.get('name')) or "", 
        'rank: ' + str(self.rank.get('name')) or "",
        'id: ' + str(self.id.get('id')) or "",
        'authority: ' + self.authority or ""
      ]
      mssg = tx + '\n  '.join(txt)
      return mssg

    def is_empty(self):
      return not self.name and not self.rank and not self.id

# def taxon(name, rank = None, id = None, authority = None):
#     '''
#     Make a taxon

#     :param name: [String] A taxonomic name
#     :param rank: [String] A rank name
#     :param id: [String] A taxonomic identifier
#     :param authority: [String] A taxonomic authority

#     :return: A dict

#     Usage::

#         from pytaxa import constructors as cs
#         name = cs.taxon_name("Poa")
#         rank = cs.taxon_rank("genus", "ncbi")
#         db = cs.taxon_database("ncbi", 
#             "http://www.ncbi.nlm.nih.gov/taxonomy",
#             "NCBI Taxonomy Database", 
#             "*")
#         id = cs.taxon_id(12345, db)
#         cs.taxon(name, rank, id, "L.")
#     '''
#     return {"name": name, "rank": rank, "id": id, "authority": authority}
