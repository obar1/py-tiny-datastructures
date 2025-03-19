def test_node(get_nodelr):
    assert get_nodelr.value == 0
    assert get_nodelr.left == None
    assert get_nodelr.right == None
    assert str(get_nodelr) == "node:0"
