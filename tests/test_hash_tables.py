def test_ht0(get_ht):
    assert (
        str(get_ht)
        == "ht:[(0, ': ', None), (1, ': ', None), (2, ': ', None), (3, ': ', None), (4, ': ', None), (5, ': ', None), (6, ': ', None)]"
    )


def test_ht(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)
    get_ht.set_item("lumber", 70)
    assert (
        str(get_ht)
        == "ht:[(0, ': ', None), (1, ': ', None), (2, ': ', None), (3, ': ', None), (4, ': ', [['bolts', 1400], ['washers', 50]]), (5, ': ', None), (6, ': ', [['lumber', 70]])]"
    )


def test_set_item(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)

    assert "1400" == str(get_ht.get_item("bolts"))
    assert "50" == str(get_ht.get_item("washers"))
    assert "None" == str(get_ht.get_item("lumber"))


def test_keys(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)
    get_ht.set_item("lumber", 70)

    assert str(get_ht.keys()) == "['bolts', 'washers', 'lumber']"
