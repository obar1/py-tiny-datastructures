def test_ds(get_q):
    assert set(["enqueue", "dequeue"]).issubset(get_q.ds_func)


def test_constrcutor(get_q):
    assert get_q.get_id == "queue"
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
