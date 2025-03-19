import pytest
from src.node import Node
from src.node_lr import NodeLR

@pytest.fixture
def get_node():
    return Node(0)


@pytest.fixture
def get_nodelr():
    return NodeLR(0)