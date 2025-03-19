def test_s(get_s):
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


def test_q(get_q):
    assert get_q.first is not None
    assert get_q.last is not None
    assert get_q.length == 1
    assert str(get_q).strip() == "q:['first:node:0,', 'node:0,', 'last:node:0,']"


def test_enqueue(get_q):
    get_q.enqueue(1)
    get_q.enqueue(2)
    assert (
        str(get_q).strip()
        == "q:['first:node:0,', 'node:0,', 'node:1,', 'node:2,', 'last:node:2,']"
    )


def test_dequeue(get_q):
    get_q.enqueue(1)
    assert str(get_q.dequeue()) == "node:0"
    assert str(get_q.dequeue()) == "node:1"
    assert str(get_q.dequeue()) == "None"
