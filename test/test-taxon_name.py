"""Tests for taxon_name"""
import os
from nose.tools import *
from pytaxa import constructors as c

def test_taxon_name():
    "taxon_name - param: name"
    res = c.taxon_name('Helianthus')
    assert dict == res.__class__
    assert 2 == len(res)
    assert 'Helianthus' == res['name']
    assert None == res['database']

def test_taxon_name_database_param():
    "taxon_name - param: name"
    res = c.taxon_name('Poa', 'ncbi')
    assert dict == res.__class__
    assert 2 == len(res)
    assert 'Poa' == res['name']
    assert 'ncbi' == res['database']
