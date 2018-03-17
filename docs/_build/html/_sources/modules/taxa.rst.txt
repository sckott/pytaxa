.. _crossref-modules:

===========
taxa module
===========

taxa module API:

* `taxon_name`

Example usage:

.. code-block:: python

    from pytaxa import Taxa
    x = Taxa()
    x.taxon_name("Poa")
    x.taxon_name("Poa", "ncbi")


taxa API
========


.. py:module:: pytaxa

.. automethod:: Taxa.taxon_name
