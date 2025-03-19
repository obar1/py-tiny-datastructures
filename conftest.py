import pytest
from src.node import Node
from src.node_lr import NodeLR
from src.linked_lists import  LinkedList
from src.doubly_linked_lists import DoublyLinkedList
from src.heaps import MaxHeap
from src.hash_tables import HashTable
from src.recursive_binary_search_trees import BinarySearchTree
from src.stacks_queues import Stack,Queue
from src.has_performance import HasPerformance
from src.recursive_binary_search_trees_traversal import BinarySearchTreeTraversal
from src.graphs import Graph

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



@pytest.fixture
def get_ht():
    return HashTable()



@pytest.fixture
def get_r_bst():
    return BinarySearchTree()


@pytest.fixture
def get_bst():
    return BinarySearchTree()

@pytest.fixture
def get_s():
    return Stack(0)

    
@pytest.fixture
def get_q():
    return Queue(0)
    
@pytest.fixture(scope="session", autouse=True)
def get_hp():
    return HasPerformance()

    
@pytest.fixture
def get_r_bst_t():
    b_rst = BinarySearchTreeTraversal()
    b_rst.insert(47)
    b_rst.insert(21)
    b_rst.insert(76)
    b_rst.insert(18)
    b_rst.insert(27)
    b_rst.insert(52)
    b_rst.insert(82)
    return b_rst

@pytest.fixture
def get_g():
    return Graph()
