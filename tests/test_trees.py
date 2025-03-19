import ipytest
import pytest


##%%ipytest


def test(get_bst):
    assert get_bst.root == None


# ---

##%%ipytest


def test(get_bst):
    get_bst.insert(1)
    assert get_bst.root != None


# ---

##%%ipytest


def test(get_bst):
    get_bst.insert(0)
    get_bst.insert(1)
    assert get_bst.contains(1)
    assert get_bst.contains(2) == False
