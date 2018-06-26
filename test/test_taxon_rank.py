"""Tests for taxon_rank"""
import os
# from nose.tools import *
import pytest
from pytaxa import constructors as c

def test_taxon_rank():
    "taxon_rank - param: name"
    res = c.taxon_rank('species')
    assert dict == res.__class__
    assert 2 == len(res)
    assert 'species' == res['name']
    assert None == res['database']

def test_taxon_rank_database_param():
    "taxon_rank - params: name & database"
    res = c.taxon_rank('genus', 'ncbi')
    assert dict == res.__class__
    assert 2 == len(res)
    assert 'genus' == res['name']
    assert 'ncbi' == res['database']
