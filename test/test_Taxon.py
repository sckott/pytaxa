"""Tests for Taxon"""
import os
# from nose.tools import *
import pytest
from pytaxa import constructors as cs
from pytaxa import Taxon

def test_Taxon():
    "Taxon"
    name = cs.taxon_name("Poa")
    rank = cs.taxon_rank("genus", "ncbi")
    db = cs.taxon_database("ncbi", 
        "http://www.ncbi.nlm.nih.gov/taxonomy",
        "NCBI Taxonomy Database", 
        "*")
    id = cs.taxon_id(12345, db)
    x = Taxon(name, rank, id, "L.")
    
    assert isinstance(x, Taxon)
    assert 'L.' == x.authority
    assert isinstance(x.authority, str)
    assert len(x.authority) > 0
    assert isinstance(x.id, dict)
    assert len(x.id) > 0
    assert isinstance(x.name, dict)
    assert len(x.name) > 0
    assert isinstance(x.rank, dict)
    assert len(x.rank) > 0
    assert x.is_empty() is False
    assert (
        '<Taxon>\n'
        '  name: Poa\n'
        '  rank: genus\n'
        '  id: 12345\n'
        '  authority: L.' == repr(x))

def test_Taxon_empty():
    "Taxon - empty"
    x = Taxon(None)
    
    assert isinstance(x, Taxon)
    assert '' == x.authority
    assert isinstance(x.authority, str)
    assert len(x.authority) == 0
    assert isinstance(x.id, dict)
    assert len(x.id) == 0
    assert isinstance(x.name, dict)
    assert len(x.name) == 0
    assert isinstance(x.rank, dict)
    assert len(x.rank) == 0
    assert x.is_empty()
    assert (
       '<Taxon>\n'
       '  name: None\n'
       '  rank: None\n'
       '  id: None\n'
       '  authority: ' == repr(x))
