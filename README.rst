=====
pygov
=====

pygov is a Python library that enables easy access to the US Government's data APIs. Read more about the available APIs `here <http://api.data.gov/docs/>`_.

Currently the only (partially) supported API is for the USDA data (specifically the Nutrient Database). Read more about the `USDA NDB API <http://ndb.nal.usda.gov/ndb/doc/>`_.

The Cesus API is brand new. The goal is to eventually support all of the available APIs to the fullest extent possible.

============
installation
============
pygov is registered with the Python Package Index so it can be installed with pip:

    pip install pygov

=====
usage
=====

    from pygov.usda.client import UsdaClient

    client = UsdaClient("DEMO_KEY")
    foods = client.list_foods(5)

    for food in foods:
        print food.name

    ...
    Abiyuch, raw
    Acerola juice, raw
    Acerola, (west indian cherry), raw
    Acorn stew (Apache)
    Agave, cooked (Southwest)