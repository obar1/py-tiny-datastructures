def test_ds(get_r_bst):
    assert set(["insert", "r_contains", "delete_node"]).issubset(get_r_bst.ds_func)


def test_constrcutor(get_r_bst_t):
    assert get_r_bst_t.get_id == "binary-search-tree"


def test_r_contains(get_r_bst):
    get_r_bst.insert(47)
    get_r_bst.insert(21)
    get_r_bst.insert(76)
    get_r_bst.insert(18)
    get_r_bst.insert(27)
    get_r_bst.insert(52)
    get_r_bst.insert(82)
    assert get_r_bst.r_contains(27)
    assert get_r_bst.r_contains(17) is False


def test_ops0(get_r_bst):
    get_r_bst.insert(2)
    get_r_bst.insert(1)
    get_r_bst.insert(3)
    assert (str(get_r_bst.root)) == "node:2"
    assert (str(get_r_bst.root.left)) == "node:1"
    assert (str(get_r_bst.root.right)) == "node:3"


def test_ops2(get_r_bst):
    get_r_bst.insert(2)
    get_r_bst.insert(1)
    get_r_bst.insert(3)
    get_r_bst.delete_node(2)
    assert (str(get_r_bst.root)) == "node:3"
    assert (str(get_r_bst.root.left)) == "node:1"
    assert (str(get_r_bst.root.right)) == "None"
    get_r_bst.delete_node(3)
    assert (str(get_r_bst.root)) == "node:1"
    assert (str(get_r_bst.root.left)) == "None"
    assert (str(get_r_bst.root.right)) == "None"


def test_convert_sorted_list_to_balanced_bst():
    """
     BST: Convert Sorted List to Balanced BST ( ** Interview Question)

    Objective:

    The task is to develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        # The 'is_balanced' and 'inorder_traversal' methods will
        # be used to test your code
        def is_balanced(self, node=None):
            def check_balance(node):
                if node is None:
                    return True, -1
                left_balanced, left_height = check_balance(node.left)
                if not left_balanced:
                    return False, 0
                right_balanced, right_height = check_balance(node.right)
                if not right_balanced:
                    return False, 0
                balanced = abs(left_height - right_height) <= 1
                height = 1 + max(left_height, right_height)
                return balanced, height

            balanced, _ = check_balance(self.root if node is None else node)
            return balanced

        def inorder_traversal(self, node=None):
            if node is None:
                node = self.root
            result = []
            self._inorder_helper(node, result)
            return result

        def _inorder_helper(self, node, result):
            if node:
                self._inorder_helper(node.left, result)
                result.append(node.value)
                self._inorder_helper(node.right, result)

        def sorted_list_to_bst(self, nums):
            self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

        def __sorted_list_to_bst(self, nums, left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            current = Node(nums[mid])

            current.left = self.__sorted_list_to_bst(nums, left, mid - 1)
            current.right = self.__sorted_list_to_bst(nums, mid + 1, right)

            return current


def test_invert_binary_tree():
    """BST: Invert Binary Tree ( ** Interview Question)

    Objective: Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.
    """

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def __r_insert(self, current_node, value):
            if current_node == None:
                return Node(value)
            if value < current_node.value:
                current_node.left = self.__r_insert(current_node.left, value)
            elif (
                value > current_node.value
            ):  # Changed to elif to avoid comparing twice if equal
                current_node.right = self.__r_insert(current_node.right, value)
            return current_node

        def r_insert(self, value):
            if self.root == None:
                self.root = Node(value)
            else:
                self.__r_insert(self.root, value)

        def invert(self):
            self.root = self.__invert_tree(self.root)

        def __invert_tree(self, node):
            if node is None:
                return None

            temp = node.left
            node.left = self.__invert_tree(node.right)
            node.right = self.__invert_tree(temp)

            return node

    def tree_to_list(node):
        """Helper function to convert tree to list level-wise for easy comparison"""
        if not node:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        while result and result[-1] is None:  # Clean up trailing None values
            result.pop()
        return result

    def test_invert_binary_search_tree():
        print("\n--- Testing Inversion of Binary Search Tree ---")
        # Define test scenarios
        scenarios = [
            ("Empty Tree", [], []),
            ("Single Node", [1], [1]),
            ("Tree with Left Child", [2, 1], [2, None, 1]),
            ("Tree with Right Child", [1, 2], [1, 2]),
            ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
            ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
        ]

        for description, setup, expected in scenarios:
            bst = BinarySearchTree()
            for num in setup:
                bst.r_insert(num)
            if description == "Invert Twice":
                bst.invert()  # First inversion
            bst.invert()  # Perform inversion (or second inversion for the specific case)
            result = tree_to_list(bst.root)
            print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
            print(f"Expected: {expected}")
            print(f"Actual:   {result}")

    test_invert_binary_search_tree()
