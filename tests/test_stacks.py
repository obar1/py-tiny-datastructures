def test_ds(get_s):
    assert set(["push", "pop"]).issubset(get_s.ds_func)


def test_constrcutor(get_s):
    assert get_s.get_id == "stack"
    assert get_s.top is not None
    assert get_s.height == 1
    assert str(get_s).strip() == "s:['top:node:0,', 'node:0,']"


def test_push0(get_s):
    get_s.push(1)
    get_s.push(2)
    assert str(get_s).strip() == "s:['top:node:2,', 'node:2,', 'node:1,', 'node:0,']"


def test_push1(get_s):
    get_s.push(1)
    assert str(get_s.pop()) == "node:1"
    assert str(get_s.pop()) == "node:0"
    assert str(get_s.pop()) == "None"
