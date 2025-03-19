def test_ds(get_g):
    assert set(["add_vertex", "add_edge", "remove_vertex"]).issubset(get_g.ds_func)


def test_g(get_g):
    assert get_g.get_id == "graph"
    assert str(get_g) == "g:[]"


def test_add_vertex0(get_g):
    get_g.add_vertex(1)
    assert str(get_g) == "g:['1:[]']"


def test_add_vertex1(get_g):
    get_g.add_vertex(1)
    get_g.add_vertex(2)
    get_g.add_edge(1, 2)
    assert str(get_g) == "g:['1:[2]', '2:[1]']"


def test_remove_vertex(get_g):
    get_g.add_vertex(1)
    get_g.add_vertex(2)
    get_g.add_edge(1, 2)
    get_g.remove_vertex(2)
    assert str(get_g) == "g:['1:[]']"
