def test_ds(get_r_bst):
    assert set(["insert", "r_contains", "delete_node"]).issubset(get_r_bst.ds_func)


def test_constrcutor(get_r_bst_t):
    assert get_r_bst_t.get_id == "binary-search-tree"


def test_r_contains(get_r_bst):
    get_r_bst.insert(47)
    get_r_bst.insert(21)
    get_r_bst.insert(76)
    get_r_bst.insert(18)
    get_r_bst.insert(27)
    get_r_bst.insert(52)
    get_r_bst.insert(82)

    assert get_r_bst.r_contains(27)
    assert get_r_bst.r_contains(17) is False


def test_ops0(get_r_bst):
    get_r_bst.insert(2)
    get_r_bst.insert(1)
    get_r_bst.insert(3)

    assert (str(get_r_bst.root)) == "node:2"
    assert (str(get_r_bst.root.left)) == "node:1"
    assert (str(get_r_bst.root.right)) == "node:3"


def test_ops2(get_r_bst):
    get_r_bst.insert(2)
    get_r_bst.insert(1)
    get_r_bst.insert(3)
    get_r_bst.delete_node(2)

    assert (str(get_r_bst.root)) == "node:3"
    assert (str(get_r_bst.root.left)) == "node:1"
    assert (str(get_r_bst.root.right)) == "None"

    get_r_bst.delete_node(3)

    assert (str(get_r_bst.root)) == "node:1"
    assert (str(get_r_bst.root.left)) == "None"
    assert (str(get_r_bst.root.right)) == "None"
