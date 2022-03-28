preimport = set(locals().keys())
from slicetime import *
postimport = set(locals().keys())
postimport.remove("preimport")

def test_exported_names():
    imported = postimport - preimport

    assert set(("time", "date", "datetime")) == imported
