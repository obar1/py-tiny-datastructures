def test_constrcutor(get_bst):
    assert get_bst.get_id == "binary-search-tree"
    assert get_bst.root is None


def test_insert(get_bst):
    get_bst.insert(1)
    assert get_bst.root is not None


def test_contains(get_bst):
    get_bst.insert(0)
    get_bst.insert(1)
    assert get_bst.contains(1)
    assert get_bst.contains(2) is False
