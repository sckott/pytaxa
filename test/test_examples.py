"""Tests for examples"""
import os
# from nose.tools import *
import pytest
from pytaxa import examples
from pytaxa import Hierarchy
from pytaxa import Taxon

def test_examples():
    "examples - poa"
    res = examples.eg_hierarchy("poa")
    assert isinstance(res, Hierarchy)
    assert isinstance(res.taxa, list)
    assert isinstance(res.taxa[0], Taxon)
    assert isinstance(res.taxa[1], Taxon)
    assert isinstance(res.taxa[2], Taxon)
    assert isinstance(res.ranklist, list)
    assert isinstance(res.xlen, int)
    assert 3 == len(res)
