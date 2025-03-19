import ipytest
import duckdb
import pytest

 
def test(get_hp):
    get_hp.save('abc')
    get_hp.save('efg')

    res = "".join(str(get_hp.con.sql("SELECT id, s FROM tbl").fetchall()))

    assert res == "[(1, 'abc'), (2, 'efg')]"
    print("".join(str(get_hp.con.sql("SELECT * FROM tbl").fetchall())))

