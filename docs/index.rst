==============================
pytaxa |version| documentation
==============================

|pypi| |travis| |coverage|

Info
====

* Minimum Python version: 3.5
* pytaxa docs_
* Check out sister R package: <https://github.com/ropensci/taxa>

.. _docs: https://focused-neumann-123664.netlify.com

Installation
============

.. toctree::
   :caption: Installation
   :hidden:

   intro/install

:doc:`intro/install`
    How to install pytaxa.

Usage
=====

.. code-block:: python

    >>> from pytaxa import constructors as cs
    >>> tn = cs.taxon_name("Poa")
    >>> tn['name']
    'Poa'

    >>> from pytaxa import Taxon
    >>> x = Taxon(None)
    >>> x.is_empty()
    True

    >>> name = cs.taxon_name("Poa")
    >>> rank = cs.taxon_rank("genus", "ncbi")
    >>> db = cs.taxon_database("ncbi",
    ...   "http://www.ncbi.nlm.nih.gov/taxonomy",
    ...   "NCBI Taxonomy Database",
    ...   "*")
    >>> id = cs.taxon_id(12345, db)
    >>> tx1 = Taxon(name, rank, id, "L.")
    >>> tx2 = Taxon(cs.taxon_name("Poaceae"),
    ...   cs.taxon_rank("family", "ncbi"), cs.taxon_id(4479, db))
    >>> tx3 = Taxon(cs.taxon_name("Poa annua"),
    ...   cs.taxon_rank("species", "ncbi"), cs.taxon_id(93036, db))
    >>> from pytaxa import Taxa
    >>> Taxa(tx1, tx2, tx3)
    <taxa>
      no. taxa: 3
      Poa / genus / 12345
      Poaceae / family / 4479
      Poa annua / species / 93036

    >>> from pytaxa import Hierarchy
    >>> out = Hierarchy(tx1, tx2, tx3)
    >>> out.taxa
    [<Taxon>
      name: Poaceae
      rank: family
      id: 4479
      authority: , <Taxon>
      name: Poa
      rank: genus
      id: 12345
      authority: L., <Taxon>
      name: Poa annua
      rank: species
      id: 93036
      authority: ]
    >>> out.ranklist
    ['180', '140', '220']
    >>> out.all_empty()
    False
    >>> out.pop(ranks = "family")
    <Hierarchy>
      Poa / genus / 12345
      Poa annua / species / 93036


Modules
=======

.. toctree::
   :caption: Modules
   :hidden:

   modules/intro
   modules/constructors
   modules/taxa
   modules/examples

:doc:`modules/intro`
    Introduction to pytaxa modules

:doc:`modules/constructors`
    The constructors module

:doc:`modules/taxa`
    The taxa module

:doc:`modules/examples`
    The examples module

All the rest
============

.. toctree::
   :caption: All the rest
   :hidden:

   changelog_link
   contributors
   contributing
   conduct
   license

:doc:`changelog_link`
    See what has changed in recent pytaxa versions.

:doc:`contributors`
    pytaxa contributors.

:doc:`contributing`
    Learn how to contribute to the pytaxa project.

:doc:`conduct`
    Expected behavior in this community. By participating in this project you agree to abide by its terms.

:doc:`license`
    The pytaxa license.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |pypi| image:: https://img.shields.io/pypi/v/pytaxa.svg
   :target: https://pypi.python.org/pypi/pytaxa

.. |travis| image:: https://travis-ci.org/sckott/pytaxa.svg
   :target: https://travis-ci.org/sckott/pytaxa

.. |coverage| image:: https://codecov.io/gh/sckott/pytaxa/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sckott/pytaxa
