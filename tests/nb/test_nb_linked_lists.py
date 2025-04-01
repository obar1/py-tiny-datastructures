# # linked list
#
# ![title](assets/image-ll0.png)
#


import sys, os

sys.path.append(os.path.abspath(".."))


from src.linked_lists import LinkedList

LinkedList(0).ds_func


# ## Leet Code style
#


def test_find_middle_node():
    """_summary_

    - Find Middle Node


    Implement the find_middle_node method for the LinkedList class.

    Note: this LinkedList implementation does not have a length member variable.

    If the linked list has an even number of nodes, return the first node of the second half of the list.
    """

    class LC(LinkedList):
        def find_middle_node(self):
            tmp = self.head
            length = 0
            while tmp:
                tmp = tmp.next
                length += 1
            tmp = self.head
            i = 1
            for i in range(length):
                if i + 1 > length // 2:
                    print(f"returned {tmp.value}")
                    return tmp
                tmp = tmp.next
                print(f"{i}/{length} {tmp.value}")

    my_linked_list = LC(1)

    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    """
    EXPECTED OUTPUT:
    ----------------
    3

    """

    assert my_linked_list.find_middle_node().value == 3


#


def test_has_loop():
    """

    - Has Loop

    Write a method called has_loop that is part of the linked list class.

    The method should be able to detect if there is a cycle or loop present in the linked list.

    You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm)
    to detect the loop.

    This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time,
    while the fast pointer moves two steps at a time.
    If there is a loop in the linked list, the two pointers will eventually meet at some point.
    If there is no loop, the fast pointer will reach the end of the list.
    """

    class LC(LinkedList):
        def has_loop(self):
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                print(f"slow {slow.value} fast {fast.value}")

                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False

    my_linked_list_1 = LC(1)
    my_linked_list_1.append(2)
    my_linked_list_1.append(3)
    my_linked_list_1.append(4)
    my_linked_list_1.tail.next = my_linked_list_1.head
    assert my_linked_list_1.has_loop()  # Returns True

    my_linked_list_2 = LC(1)
    my_linked_list_2.append(2)
    my_linked_list_2.append(3)
    my_linked_list_2.append(4)
    assert (my_linked_list_2.has_loop()) == False


def test_find_kth_node_from_end():
    """
        - Find Kth Node From End

    Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

    Given this LinkedList:

    1 -> 2 -> 3 -> 4

    If k=1 then return the first node from the end (the last node) which contains the value of 4.

    If k=2 then return the second node from the end which contains the value of 3, etc.

    If the index is out of bounds, the program should return None.
    """


from src.nodes import Node


class LC(LinkedList):
    @staticmethod
    def find_kth_from_end(ll, k):
        slow = fast = ll.head
        try:
            while 1 == 1:
                for _ in range(k):
                    fast = fast.next
                slow = slow.next
        except:
            return slow.next


my_linked_list = LC(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
assert str(LC.find_kth_from_end(my_linked_list, k)) == str(Node(4))


def test_partition_list():
    """
    Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

    Note:  This linked list class does NOT have a tail which will make this method easier to implement.

    The original relative order of the nodes should be preserved.


    Details:

    The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.


    """

    class LC(LinkedList):

        def partition_list(self, x):
            if not self.head:
                return None

            dummy1 = Node(0)
            dummy2 = Node(0)
            prev1 = dummy1
            prev2 = dummy2
            current = self.head

            while current:
                if current.value < x:
                    prev1.next = current
                    prev1 = current
                else:
                    prev2.next = current
                    prev2 = current
                current = current.next

            prev1.next = None
            prev2.next = None
            prev1.next = dummy2.next

            self.head = dummy1.next

    def linkedlist_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    ll = LC(3)
    x = 3
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    ll.partition_list(x)
    assert linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]

    ll = LC(3)
    ll.append(3)
    ll.append(3)

    ll.partition_list(x)
    assert linkedlist_to_list(ll.head) == [3, 3, 3]


def test_remove_duplicates():
    """

    LL: Remove Duplicates ( ** Interview Question)

    You are given a singly linked list that contains integer values, where some of these values may be duplicated.

    Note: this linked list class does NOT have a tail which will make this method easier to implement.

    Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

    """

    class LC(LinkedList):
        def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next

    ll = LC(1)
    ll.append(2)
    ll.append(3)
    ll.remove_duplicates()
    assert str(ll) == "ll:['node:1,', 'node:2,', 'node:3,']"

    ll = LC(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    ll.append(2)
    ll.remove_duplicates()
    assert str(ll) == "ll:['node:1,', 'node:2,', 'node:3,']"


def test_binaryto_decimal():
    """


    LL: Binary to Decimal ( ** Interview Question)

    Your task is to implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

    In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.
    """


class LC(LinkedList):
    def binary_to_decimal(self):
        decimalValue = 0
        temp = self.head
        while temp != None:
            # Left shift current decimal value by 1 and OR with current node's value
            # decimalValue = (decimalValue << 1) | temp.value;
            decimalValue = decimalValue * 2 + temp.value
            temp = temp.next

        return decimalValue


linked_list = LC(1)
result = linked_list.binary_to_decimal()
assert linked_list.binary_to_decimal() == 1

linked_list = LC(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
assert linked_list.binary_to_decimal() == 13
