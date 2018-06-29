"""Tests for Hierarchy"""
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

def test_print_taxon():
    assert 'empty' == Hierarchy.print_taxon(Taxon())
    assert 'Poa annua / species / 93036' == Hierarchy.print_taxon(tx3)
