def test_consturctor(get_ll):
    assert get_ll.head != None
    assert get_ll.tail != None
    assert get_ll.length == 1
    assert str(get_ll).strip() == "ll:['node:0,']"


# ---

# %%ipytest


def test_append(get_ll):
    get_ll.append(1)
    get_ll.append(2)
    assert str(get_ll).strip() == "ll:['node:0,', 'node:1,', 'node:2,']"


# ---

## %%ipytest


def test_pop(get_ll):
    assert str(get_ll.pop()) == "node:0"
    assert str(get_ll.pop()) == "None"


# ---

## %%ipytest


def test_prepend(get_ll):
    get_ll.append(1)
    get_ll.prepend(2)
    assert str(get_ll).strip() == "ll:['node:2,', 'node:0,', 'node:1,']"


# ---

## %%ipytest


def test_get(get_ll):
    assert str(get_ll.get(0)) == "node:0"
    assert str(get_ll.get(1)) == "None"


# ---

## %%ipytest


def test_set(get_ll):
    get_ll.set_value(0, "A")
    assert str(get_ll.get(0)) == "node:A"


# %%
