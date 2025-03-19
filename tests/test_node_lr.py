def test_node(get_nodelr):
    assert get_nodelr.value == 0
    assert get_nodelr.left is None
    assert get_nodelr.right is None
    assert str(get_nodelr) == "node:0"
