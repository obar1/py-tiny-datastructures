def test_node(get_node):
    assert get_node.value == 0
    assert get_node.next is None
    assert str(get_node) == "node:0"
