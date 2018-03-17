import sys

class Taxa(object):
    '''
    Taxa: Class for Taxonomic names

    |
    |
    |

    **Included methods**

    * /taxon_name - :func:`~pytaxa.Taxa.taxon_name`

    |
    |
    |
    '''
    def __init__(self):
        pass

    def taxon_name(self, name, database = None):
        '''
        Make a taxon name

        :param name: [Array] A taxonomic name
        :param database: [String] A database name

        :return: A dict

        Usage::

            from pytaxa import Taxa
            x = Taxa()
            x.taxon_name("Poa")
            x.taxon_name("Poa", "ncbi")
        '''
        return {"name": name, "database": database}
