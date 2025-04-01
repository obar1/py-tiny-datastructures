from src.doubly_linked_lists import DoublyLinkedList

from src.nodes import NodeP as Node


def test_swap_firstand_ast():
    """
    # Swap First and Last


    DLL: Swap First and Last ( ** Interview Question)


    Swap the values of the first and last node


    Method name:
    swap_first_last


    Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.




    """

    class LC(DoublyLinkedList):

        def swap_first_last(self):
            if self.length == 0:
                return
            self.head.value, self.tail.value = self.tail.value, self.head.value

    my_doubly_linked_list = LC(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)

    print("DLL before swap_first_last():")
    assert (
        str(my_doubly_linked_list) == "dll:['node:1,', 'node:2,', 'node:3,', 'node:4,']"
    )

    my_doubly_linked_list.swap_first_last()

    print("\nDLL after swap_first_last():")
    assert (
        str(my_doubly_linked_list) == "dll:['node:4,', 'node:2,', 'node:3,', 'node:1,']"
    )


def test_reserve():
    """


    DLL: Reverse ( ** Interview Question)


    Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.


    """

    class LC(DoublyLinkedList):
        def reverse(self):
            temp = self.head
            while temp is not None:
                # swap the prev and next pointers of node points to
                temp.prev, temp.next = temp.next, temp.prev

                # move to the next node
                temp = temp.prev

            # swap the head and tail pointers
            self.head, self.tail = self.tail, self.head

    my_doubly_linked_list = LC(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)

    print("DLL before reverse():")
    assert (
        str(my_doubly_linked_list) == "dll:['node:1,', 'node:2,', 'node:3,', 'node:4,']"
    )

    my_doubly_linked_list.reverse()

    print("\nDLL after reverse():")
    assert (
        str(my_doubly_linked_list) == "dll:['node:4,', 'node:3,', 'node:2,', 'node:1,']"
    )


def test_palindrome_checker():
    """


    DLL: Palindrome Checker ( ** Interview Question)


    Write a method to determine whether a given doubly linked list reads the same forwards and backwards.


    For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.


    If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.


    """

    class LC(DoublyLinkedList):
        def is_palindrome(self):
            l = self.length
            if l <= 1:
                return True
            sx = self.head
            dx = self.tail
            try:
                for i in range(l):
                    assert sx.value == dx.value
                    sx = sx.next
                    dx = dx.prev
                    if i > l // 2:
                        return True
            except:
                return False
            return False

    my_dll_1 = LC(1)
    my_dll_1.append(2)
    my_dll_1.append(3)
    my_dll_1.append(2)
    my_dll_1.append(1)

    print("my_dll_1 is_palindrome:")
    assert my_dll_1.is_palindrome()

    my_dll_2 = LC(1)
    my_dll_2.append(2)
    my_dll_2.append(3)

    print("\nmy_dll_2 is_palindrome:")
    assert my_dll_2.is_palindrome() is False


def test_swap_nodesin_pairs():
    """
    DLL: Swap Nodes in Pairs
    Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list.
    The method should not take any input parameters.
    """

    class LC(DoublyLinkedList):
        def swap_pairs(self):
            dummy_node = Node(0)
            dummy_node.next = self.head
            previous_node = dummy_node

            while self.head and self.head.next:
                first_node = self.head
                second_node = self.head.next

                previous_node.next = second_node
                first_node.next = second_node.next
                second_node.next = first_node

                second_node.prev = previous_node
                first_node.prev = second_node

                if first_node.next:
                    first_node.next.prev = first_node

                self.head = first_node.next
                previous_node = first_node

            self.head = dummy_node.next

            if self.head:
                self.head.prev = None

    my_dll = LC(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)
    print("my_dll before swap_pairs:")
    assert str(my_dll) == "dll:['node:1,', 'node:2,', 'node:3,', 'node:4,']"
    print("my_dll after swap_pairs:")
    my_dll.swap_pairs()
    assert str(my_dll) == "dll:['node:2,', 'node:1,', 'node:4,', 'node:3,']"
