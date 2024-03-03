from src.utils import *

def test_load_operations():
    assert load_operations() != []
    assert load_operations() != False
    assert load_operations() != ""
