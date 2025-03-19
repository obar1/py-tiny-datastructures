import ipytest
import pytest


def test_h(get_mh):
    assert str(get_mh) == "mh:[]"


# ---

##%%ipytest -vv


def test_insert(get_mh):
    get_mh.insert(99)
    get_mh.insert(72)
    get_mh.insert(61)
    get_mh.insert(58)
    assert (
        str(get_mh) == "mh:[(0, ': ', 99), (1, ': ', 72), (2, ': ', 61), (3, ': ', 58)]"
    )
    get_mh.insert(100)
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 100), (1, ': ', 99), (2, ': ', 61), (3, ': ', 58), (4, ': ', 72)]"
    )
    get_mh.insert(75)
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 100), (1, ': ', 99), (2, ': ', 75), (3, ': ', 58), (4, ': ', 72), (5, ': ', 61)]"
    )


# ---

##%%ipytest -vv


def test_remove(get_mh):
    for i in [95, 75, 80, 55, 60, 50, 65]:
        get_mh.insert(i)
    get_mh.remove()
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 80), (1, ': ', 75), (2, ': ', 65), (3, ': ', 55), (4, ': ', 60), (5, ': ', 50)]"
    )
    get_mh.remove()
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 75), (1, ': ', 60), (2, ': ', 65), (3, ': ', 55), (4, ': ', 50)]"
    )
