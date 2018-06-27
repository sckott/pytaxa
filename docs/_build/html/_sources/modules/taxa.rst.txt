.. _taxa-modules:

===========
taxa module
===========

taxa module API:

* `Taxon`
* `Taxa`
* `Hierarchy`
* `Hierarchies`

Example usage:

.. code-block:: python

    # make a taxon
    from pytaxa import constructors as cs
    name = cs.taxon_name("Poa")
    rank = cs.taxon_rank("genus", "ncbi")
    db = cs.taxon_database("ncbi", 
        "http://www.ncbi.nlm.nih.gov/taxonomy",
        "NCBI Taxonomy Database", 
        "*")
    id = cs.taxon_id(12345, db)
    tx = cs.taxon(name, rank, id, "L.")
    
    # combine many taxon's into taxa
    from pytaxa import Taxa
    Taxa(tx)
    bb = Taxa(tx, tx)


taxa API
========

.. py:module:: pytaxa

.. autoclass:: Taxon
.. autoclass:: Taxa
.. autoclass:: Hierarchy
.. autoclass:: Hierarchies


.. _hierarchy-methods:

Hierarchy functions
===================

.. py:module:: pytaxa

.. automethod:: Hierarchy.all_empty
.. automethod:: Hierarchy.pop
.. automethod:: Hierarchy.pick
