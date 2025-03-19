from src.a_ds import ADS
from src.node_lr import NodeLR as Node
class BinarySearchTree(ADS):
    @property
    def get_id(self):
        return "binary-search-tree"
    def __init__(self):
        self.root = None
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        return False
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value
    def _delete_recursive(self, node, value):
        # Base case: Empty tree
        if node is None:
            return None
        # Find the node to delete
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Handle different cases of node deletion
            # Case 1: No children
            if node.left is None and node.right is None:
                return None
            # Case 2: One child (right child exists)
            if node.left is None:
                return node.right
            # Case 2: One child (left child exists)
            if node.right is None:
                return node.left
            # Case 3: Two children
            min_value = self._find_min(node.right)
            node.value = min_value
            node.right = self._delete_recursive(node.right, min_value)
        return node
    def delete_node(self, value):
        self.root = self._delete_recursive(self.root, value)
