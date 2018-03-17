.. _constructors-modules:

===================
constructors module
===================

constructors module API:

* `taxon_database`
* `taxon_name`
* `taxon_rank`
* `taxon_id`

Example usage:

.. code-block:: python

    from pytaxa import constructors as cs
    cs.taxon_database("ncbi", 
        "http://www.ncbi.nlm.nih.gov/taxonomy",
        "NCBI Taxonomy Database", 
        "*")


constructors API
================

.. py:module:: pytaxa

.. automethod:: constructors.taxon_database
.. automethod:: constructors.taxon_name
.. automethod:: constructors.taxon_rank
.. automethod:: constructors.taxon_id
