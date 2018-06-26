"""Tests for taxon_id"""
import os
# from nose.tools import *
import pytest
from pytaxa import constructors as c

def test_taxon_id():
    "taxon_id - param: id"
    res = c.taxon_id(12345)
    assert dict == res.__class__
    assert 2 == len(res)
    assert 12345 == res['id']
    assert None == res['database']

def test_taxon_id_database_param():
    "taxon_id - params: id & database"
    res = c.taxon_id(12345, 'ncbi')
    assert dict == res.__class__
    assert 2 == len(res)
    assert 12345 == res['id']
    assert 'ncbi' == res['database']
