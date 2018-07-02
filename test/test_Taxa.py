"""Tests for Taxa"""
import os
# from nose.tools import *
import pytest
from pytaxa import constructors as cs
from pytaxa import Taxa,Taxon,Hierarchy

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

def test_Taxa():
    "Taxa"
    x = Taxa(tx3, tx1, tx2)
    
    assert isinstance(x, Taxa)
    assert isinstance(x.taxa, list)
    assert isinstance(x.taxa[0], Taxon)
    assert isinstance(x.taxa[1], Taxon)
    assert isinstance(x.taxa[2], Taxon)
    assert isinstance(x.xlen, int)
    assert 3 == len(x)
    assert (
        '<taxa>\n'
        '  no. taxa: 3\n'
        '  Poa annua / species / 93036\n'
        '  Poaceae / family / 4479\n'
        '  Poa / genus / 12345' == repr(x))

def test_Taxa_empty():
    "Taxa - empty"
    x = Taxa(Taxon())
    
    assert isinstance(x, Taxa)
    assert isinstance(x.taxa, list)
    assert isinstance(x.taxa[0], Taxon)
    assert x.taxa[0].is_empty()
    assert isinstance(x.xlen, int)
    assert 1 == len(x)
    assert '<taxa>\n  no. taxa: 1\n  empty' == repr(x)
