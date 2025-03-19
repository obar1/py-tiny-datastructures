



#---

##%%ipytest

def test_g(get_g):
    assert str(get_g) == "g:[]"

#---

##%%ipytest

def test_node(get_g):
    get_g.add_vertex(1)
    assert str(get_g) == "g:['1:[]']"

#---

##%%ipytest

def test_node(get_g):
    get_g.add_vertex(1)
    get_g.add_vertex(2)
    get_g.add_edge(1,2)
    assert str(get_g) == "g:['1:[2]', '2:[1]']"

#---

##%%ipytest

def test_node(get_g):
    get_g.add_vertex(1)
    get_g.add_vertex(2)
    get_g.add_edge(1,2)
    get_g.remove_vertex(2)
    assert str(get_g) == "g:['1:[]']"
