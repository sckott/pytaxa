"""Tests for taxon_database"""
import os
from nose.tools import *
from pytaxa import constructors as c

def test_taxon_database():
    "taxon_database - param: database"
    res = c.taxon_database('ncbi')
    assert dict == res.__class__
    assert 4 == len(res)
    assert 'ncbi' == res['database']

def test_taxon_database_other_params():
    "taxon_database - param: all"
    res = c.taxon_database("ncbi", 
            "http://www.ncbi.nlm.nih.gov/taxonomy",
            "NCBI Taxonomy Database", 
            "*")
    assert dict == res.__class__
    assert 4 == len(res)
    assert 'ncbi' == res['database']
    assert "http://www.ncbi.nlm.nih.gov/taxonomy" == res['url']
    assert "NCBI Taxonomy Database" == res['description']
    assert "*" == res['id_regex']
