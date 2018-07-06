"""Tests for Hierarchy"""
from copy import copy
import pytest
from pytaxa import constructors as cs
from pytaxa import Taxon,Hierarchy

db = cs.taxon_database("ncbi", 
    "http://www.ncbi.nlm.nih.gov/taxonomy",
    "NCBI Taxonomy Database", 
    "*")

# make some taxon's
tx1 = Taxon(cs.taxon_name("Poaceae"), 
  cs.taxon_rank("family", "ncbi"), cs.taxon_id(4479, db))
tx2 = Taxon(cs.taxon_name("Poa"), 
  cs.taxon_rank("genus", "ncbi"), cs.taxon_id(12345, db))
tx3 = Taxon(cs.taxon_name("Poa annua"), 
  cs.taxon_rank("species", "ncbi"), cs.taxon_id(93036, db))

def test_Hierarchy():
    "Hierarchy"
    x = Hierarchy(tx3, tx1, tx2)
    
    assert isinstance(x, Hierarchy)
    assert isinstance(x.taxa, list)
    assert isinstance(x.taxa[0], Taxon)
    assert isinstance(x.taxa[1], Taxon)
    assert isinstance(x.taxa[2], Taxon)
    assert isinstance(x.ranklist, list)
    assert isinstance(x.xlen, int)
    assert 3 == len(x)

def test_Hierarchy_pick():
    x = Hierarchy(tx3, tx1, tx2)

    with pytest.raises(ValueError):
        copy(x).pick()
    assert 1 == len(copy(x).pick(ranks='family'))
    assert 1 == len(copy(x).pick(ranks='genus'))
    assert 1 == len(copy(x).pick(ranks='species'))
    assert 2 == len(copy(x).pick(names='Poaceae'))
    assert 1 == len(copy(x).pick(names='Poa'))
    assert 2 == len(copy(x).pick(names='Poa annua'))
    assert 1 == len(copy(x).pick(ids=4479))
    assert 1 == len(copy(x).pick(ids=12345))
    assert 1 == len(copy(x).pick(ids=93036))

    with pytest.raises(ValueError):
        Hierarchy().pick()

def test_Hierarchy_pop():
    x = Hierarchy(tx3, tx1, tx2)

    with pytest.raises(ValueError):
        x.pop()

    x.pop(ranks='FAKE')
    assert 3 == len(x)
    x.pop(ranks='genus')
    assert 2 == len(x)

    x.pop(names='FAKE')
    assert 2 == len(x)
    x.pop(names=['FAKE', 'Poaceae'])
    assert 1 == len(x)

    x.pop(ids=0)
    assert 1 == len(x)
    x.pop(ids=[0, 93036])
    assert 0 == len(x)

def test_Hierarchy_empty():
    "Hierarchy - empty"
    x = Hierarchy(Taxon())
    
    assert isinstance(x, Hierarchy)
    assert isinstance(x.taxa, tuple)
    assert isinstance(x.taxa[0], Taxon)
    assert x.taxa[0].is_empty()
    assert x.ranklist is None
    assert isinstance(x.xlen, int)
    assert 1 == len(x)
    with pytest.raises(ValueError):
        x.pop()
