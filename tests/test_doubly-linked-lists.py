


#---

##%%ipytest

def test_consturctor(get_dll):
    assert get_dll.head != None
    assert get_dll.tail != None 
    assert get_dll.length == 1 
    assert str(get_dll).strip() == "dll:['node:0,']"

#---

##%%ipytest

def test_append(get_dll):
    get_dll.append(1)
    get_dll.append(2)
    assert str(get_dll).strip() == "dll:['node:0,', 'node:1,', 'node:2,']"

#---

##%%ipytest

def test_pop(get_dll):
    assert str(get_dll.pop()) == "node:0"
    assert str(get_dll.pop()) == "None"

#---

##%%ipytest

def test_prepend(get_dll):
    get_dll.append(1)
    get_dll.prepend(2)
    assert str(get_dll).strip() == "dll:['node:2,', 'node:0,', 'node:1,']"

#---

##%%ipytest

def test_get(get_dll):
    assert str(get_dll.get(0)) == "node:0"
    assert str(get_dll.get(1)) == "None"

#---

##%%ipytest

def test_insert(get_dll):
    get_dll.insert(0,'A')
    assert str(get_dll.get(0)) == "node:A"

#---

##%%ipytest

def test_remove(get_dll):
    get_dll.append(1)
    get_dll.append(2)
    get_dll.remove(1)
    assert str(get_dll).strip() == "dll:['node:0,', 'node:2,']"
    get_dll.remove(1)
    assert str(get_dll).strip() == "dll:['node:0,']"

 