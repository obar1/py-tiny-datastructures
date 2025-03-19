def test_ds(get_r_bst_t):
    assert set(["bfs", "dfs_pre_order", "dfs_post_order", "dfs_in_order"]).issubset(
        get_r_bst_t.ds_func
    )


def test_constrcutor(get_r_bst_t):
    assert get_r_bst_t.get_id == "binary-search-tree"


def test_bfs(get_r_bst_t):
    assert str(get_r_bst_t.bfs()) == "[47, 21, 76, 18, 27, 52, 82]"


def test_dfs_pre_order(get_r_bst_t):
    assert str(get_r_bst_t.dfs_pre_order()) == "[47, 21, 18, 27, 76, 52, 82]"


def test_dfs_post_order(get_r_bst_t):
    assert str(get_r_bst_t.dfs_post_order()) == "[18, 27, 21, 52, 82, 76, 47]"


def test_dfs_in_order(get_r_bst_t):
    assert str(get_r_bst_t.dfs_in_order()) == "[18, 21, 27, 47, 52, 76, 82]"
