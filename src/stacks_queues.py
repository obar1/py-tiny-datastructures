from src.a_ds import ADS
from src.nodes import Node


class Stack(ADS):
    @property
    def get_id(self):
        return "stack"

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def _get_repr(self):
        yield f"top:{self.top},"
        temp = self.top
        while temp is not None:
            yield str(temp) + ","
            temp = temp.next

    def __repr__(self):
        return f"s:{list(self._get_repr())}"

    def push(self, value):
        new_node = Node(value)
        try:
            assert self.top
            new_node.next = self.top
            self.top = new_node
        except AssertionError:
            self.top = new_node
        finally:
            self.height += 1

    def pop(self):
        try:
            assert self.top
            tmp = self.top
            self.top = tmp.next
            tmp.next = None
            return tmp
        except AssertionError:
            return None
        finally:
            self.height -= 1


class StackL(ADS):
    """Stack with a List"""

    @property
    def get_id(self):
        return "stack with list"

    def __init__(self):
        self.stack_list = []

    def _get_repr(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            yield self.stack_list[i]

    def __repr__(self):
        return f"s:{list(self._get_repr())}"

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class Queue(ADS):
    @property
    def get_id(self):
        return "queue"

    def __init__(self, value):
        nn = Node(value)
        self.first = self.last = nn
        self.length = 1

    def print_list(self):
        yield f"first:{self.first},"
        temp = self.first
        while temp is not None:
            yield str(temp) + ","
            temp = temp.next
        yield f"last:{self.last},"

    def __repr__(self):
        return f"q:{list(self.print_list())}"

    def enqueue(self, value):
        nn = Node(value)
        try:
            assert self.first
            self.last.next = nn
            self.last = nn
        except AssertionError:
            self.first = nn
            self.last = nn
        finally:
            self.length += 1

    def dequeue(self):
        tmp = self.first
        try:
            assert tmp
        except AssertionError:
            return None
        finally:
            self.length -= 1
        self.first = self.first.next
        if self.length == 1:
            self.last = None
        tmp.next = None
        return tmp
