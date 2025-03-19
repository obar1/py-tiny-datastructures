import pytest
from src.node import Node
from src.node_lr import NodeLR
from src.linked_lists import  LinkedList
from src.doubly_linked_lists import DoublyLinkedList
from src.heaps import MaxHeap

@pytest.fixture
def get_node():
    return Node(0)


@pytest.fixture
def get_nodelr():
    return NodeLR(0)


@pytest.fixture
def get_ll():
    return LinkedList(0)


@pytest.fixture
def get_dll():
    return DoublyLinkedList(0)
    


@pytest.fixture
def get_mh():
    return MaxHeap()