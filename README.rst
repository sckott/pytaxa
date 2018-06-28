pytaxa
======

|pypi| |travis| |coverage|

info
====

* Minimum Python version: 3.5
* pytaxa `docs <https://focused-neumann-123664.netlify.com/>`_
* Check out sister R package: `taxa <https://github.com/ropensci/taxa>`_

Installation
============

Stable version

.. code-block:: console

    pip install pytaxa
    pip3 install pytaxa

Dev version

.. code-block:: console

    sudo pip install git+git://github.com/sckott/pytaxa.git#egg=pytaxa

    # OR

    git clone git@github.com:sckott/pytaxa.git
    cd pytaxa
    make install

Usage
=====

.. code-block:: python

    from pytaxa import constructors as cs
    cs.taxon_name("Poa")
    
    from pytaxa import Taxon
    x = Taxon(None)
    x.is_empty()

    name = cs.taxon_name("Poa")
    rank = cs.taxon_rank("genus", "ncbi")
    db = cs.taxon_database("ncbi", 
      "http://www.ncbi.nlm.nih.gov/taxonomy",
      "NCBI Taxonomy Database", 
      "*")
    id = cs.taxon_id(12345, db)
    tx1 = Taxon(name, rank, id, "L.")
    tx2 = Taxon(cs.taxon_name("Poaceae"), 
      cs.taxon_rank("family", "ncbi"), cs.taxon_id(4479, db))
    tx3 = Taxon(cs.taxon_name("Poa annua"), 
      cs.taxon_rank("species", "ncbi"), cs.taxon_id(93036, db))
    from pytaxa import Taxa
    Taxa(tx1, tx2, tx3)

    from pytaxa import Hierarchy
    out = Hierarchy(tx1, tx2, tx3)
    out.taxa
    out.ranklist
    out.all_empty()
    out.pop(ranks = "family")

Contributing
============

See `CONTRIBUTING.md <https://github.com/sckott/pytaxa/blob/master/.github/CONTRIBUTING.md>`_

Meta
====

* Please note that this project is released with a `Contributor Code of Conduct <https://github.com/sckott/pytaxa/blob/master/CODE_OF_CONDUCT.md>`__. By participating in this project you agree to abide by its terms.
* License: MIT; see `LICENSE file <https://github.com/sckott/pytaxa/blob/master/LICENSE>`__

.. |pypi| image:: https://img.shields.io/pypi/v/pytaxa.svg
   :target: https://pypi.python.org/pypi/pytaxa

.. |travis| image:: https://travis-ci.org/sckott/pytaxa.svg?branch=master
   :target: https://travis-ci.org/sckott/pytaxa

.. |coverage| image:: https://codecov.io/gh/sckott/pytaxa/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sckott/pytaxa

