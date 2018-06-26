from ..constructors import constructors as cs
from ..taxa import Taxon,Hierarchy

def eg_hierarchy(which = "poa"):
  """
    Hierarchy example objects

    Usage:::
        
        from pytaxa import examples
        examples.eg_hierarchy("poa")
        examples.eg_hierarchy("puma")
        examples.eg_hierarchy("salmo")
  """
  if which not in ['poa', 'puma', 'salmo']:
    raise ValueError("'which' must be one of 'poa', 'puma', or 'salmo'")

  db = cs.taxon_database("ncbi", 
      "http://www.ncbi.nlm.nih.gov/taxonomy",
      "NCBI Taxonomy Database", 
      "*")
  
  if which == "poa":
    tx1 = Taxon(cs.taxon_name("Poaceae"), 
      cs.taxon_rank("family", "ncbi"), cs.taxon_id(4479, db))
    tx2 = Taxon(cs.taxon_name("Poa"), 
      cs.taxon_rank("genus", "ncbi"), cs.taxon_id(12345, db))
    tx3 = Taxon(cs.taxon_name("Poa annua"), 
      cs.taxon_rank("species", "ncbi"), cs.taxon_id(93036, db))
    return Hierarchy(tx3, tx1, tx2)
  elif which == "puma":
    tx1 = Taxon(cs.taxon_name("Felidae"), 
      cs.taxon_rank("family", "ncbi"), cs.taxon_id(9681, db))
    tx2 = Taxon(cs.taxon_name("Puma"), 
      cs.taxon_rank("genus", "ncbi"), cs.taxon_id(146712, db))
    tx3 = Taxon(cs.taxon_name("Puma concolor"), 
      cs.taxon_rank("species", "ncbi"), cs.taxon_id(9696, db))
    return Hierarchy(tx3, tx1, tx2)
  else:
    tx1 = Taxon(cs.taxon_name("Chordata"), 
      cs.taxon_rank("phylum", "ncbi"), cs.taxon_id(158852, db))
    tx2 = Taxon(cs.taxon_name("Vertebrata"), 
      cs.taxon_rank("subphylum", "ncbi"), cs.taxon_id(331030, db))
    tx3 = Taxon(cs.taxon_name("Teleostei"), 
      cs.taxon_rank("class", "ncbi"), cs.taxon_id(161105, db))
    tx4 = Taxon(cs.taxon_name("Salmonidae"), 
      cs.taxon_rank("family", "ncbi"), cs.taxon_id(161931, db))
    tx5 = Taxon(cs.taxon_name("Salmo"), 
      cs.taxon_rank("genus", "ncbi"), cs.taxon_id(161994, db))
    tx6 = Taxon(cs.taxon_name("Salmo salar"), 
      cs.taxon_rank("species", "ncbi"), cs.taxon_id(161996, db))
    return Hierarchy(tx1, tx2, tx3, tx4, tx5, tx6)

