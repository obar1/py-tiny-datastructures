from src.recursive_binary_search_trees_traversal import BinarySearchTreeTraversal


# ---


# ---

##%%ipytest


def test(get_r_bst_t):
    assert str(get_r_bst_t.bfs()) == "[47, 21, 76, 18, 27, 52, 82]"


# ---

##%%ipytest


def test(get_r_bst_t):
    assert str(get_r_bst_t.dfs_pre_order()) == "[47, 21, 18, 27, 76, 52, 82]"


# ---

##%%ipytest


def test(get_r_bst_t):
    assert str(get_r_bst_t.dfs_post_order()) == "[18, 27, 21, 52, 82, 76, 47]"


# ---

##%%ipytest


def test(get_r_bst_t):
    assert str(get_r_bst_t.dfs_in_order()) == "[18, 21, 27, 47, 52, 76, 82]"
