from src.stacks_queues import StackL


def test_s(get_s):
    assert set(["push", "pop"]).issubset(get_s.ds_func)


def test_constrcutor_s(get_s):
    assert get_s.get_id == "stack"
    assert get_s.top is not None
    assert get_s.height == 1
    assert str(get_s).strip() == "s:['top:node:0,', 'node:0,']"


def test_push0(get_s):
    get_s.push(1)
    get_s.push(2)
    assert str(get_s).strip() == "s:['top:node:2,', 'node:2,', 'node:1,', 'node:0,']"


def test_push1(get_s):
    get_s.push(1)
    assert str(get_s.pop()) == "node:1"
    assert str(get_s.pop()) == "node:0"
    assert str(get_s.pop()) == "None"


def test_q(get_q):
    assert set(["enqueue", "dequeue"]).issubset(get_q.ds_func)


def test_constrcutor_q(get_q):
    assert get_q.get_id == "queue"
    assert get_q.first is not None
    assert get_q.last is not None
    assert get_q.length == 1
    assert str(get_q).strip() == "q:['first:node:0,', 'node:0,', 'last:node:0,']"


def test_enqueue(get_q):
    get_q.enqueue(1)
    get_q.enqueue(2)
    assert (
        str(get_q).strip()
        == "q:['first:node:0,', 'node:0,', 'node:1,', 'node:2,', 'last:node:2,']"
    )


def test_dequeue(get_q):
    get_q.enqueue(1)
    assert str(get_q.dequeue()) == "node:0"
    assert str(get_q.dequeue()) == "node:1"
    assert str(get_q.dequeue()) == "None"


# # Stack & Queues
#


# ## Leet Code style
#


def test_0():
    """
    # Stack: Push for Stack That Uses List ( ** Interview Question)


    Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.




    """

    my_stack = StackL()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    assert str(my_stack) == "s:[3, 2, 1]"


def test_1():
    """


    #  Stack: Pop for Stack That Uses List ( ** Interview Question)
    Stack: Pop for Stack That Uses List ( ** Interview Question)


    Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.


    """

    my_stack = StackL()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert str(my_stack) == "s:[3, 2, 1]"

    print("\nPopped node:")
    print(my_stack.pop())

    print("\nStack after pop():")
    assert str(my_stack) == "s:[2, 1]"


def test_2():
    """
    #  Stack: Parentheses Balanced ( ** Interview Question)

    Check to see if a string of parentheses is balanced or not.
    By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.
    """


def is_balanced_parentheses(s):
    stack = StackL()
    bracket_pairs = {"(": ")"}
    try:
        for c in s:
            if c in bracket_pairs.keys():
                stack.push(c)
            else:
                if c != bracket_pairs[stack.pop()]:
                    return False
        assert stack.size() == 0
    except:
        return False
    return True


assert is_balanced_parentheses("((()))") is True
assert is_balanced_parentheses("()") is True
assert is_balanced_parentheses("(()())") is True
assert is_balanced_parentheses("(()") is False
assert is_balanced_parentheses("())") is False
assert is_balanced_parentheses(")(") is False
assert is_balanced_parentheses("") is True
assert is_balanced_parentheses("()()()()") is True
assert is_balanced_parentheses("(())(())") is True
assert is_balanced_parentheses("(()()())") is True
assert is_balanced_parentheses("((())") is False


def test_3():
    """

    Stack: Reverse String ( ** Interview Question)

    The reverse_string function takes a single parameter string, which is the string you want to reverse.
    """

    def reverse_string(txt):
        s = StackL()
        for c in txt:
            s.push(c)
        return "".join([s.pop() for _ in txt])

    my_string = "hello"
    assert reverse_string(my_string) == "olleh"

    my_string = ""
    assert reverse_string(my_string) == ""


def test_4():
    """

    Stack: Sort String ( ** Interview Question)

    Sort with stack
    """

    def sort_string(input_str):
        stack1 = StackL()
        stack2 = StackL()

        for char in input_str:
            stack1.push(char)

        while not stack1.is_empty():
            temp = stack1.pop()
            # Move elements from stack2 back to stack1 until we find correct position
            while not stack2.is_empty() and stack2.peek() > temp:
                stack1.push(stack2.pop())

            stack2.push(temp)

        sorted_str = ""
        while not stack2.is_empty():
            sorted_str = stack2.pop() + sorted_str  # Add to beginning instead of end

        return "".join(sorted_str)

    # Test cases
    test_strings = ["dcba", "hello", "python", "zyxwvu"]
    for test_str in test_strings:
        assert "".join(sorted(test_str)) == sort_string(test_str)
