from src.heaps import MaxHeap


def test_ds(get_mh):
    assert set(["insert", "remove"]).issubset(get_mh.ds_func)


def test_constrcutor(get_mh):
    assert get_mh.get_id == "max-heap"
    assert str(get_mh) == "mh:[]"


def test_insert(get_mh):
    get_mh.insert(99)
    get_mh.insert(72)
    get_mh.insert(61)
    get_mh.insert(58)
    assert (
        str(get_mh) == "mh:[(0, ': ', 99), (1, ': ', 72), (2, ': ', 61), (3, ': ', 58)]"
    )
    get_mh.insert(100)
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 100), (1, ': ', 99), (2, ': ', 61), (3, ': ', 58), (4, ': ', 72)]"
    )
    get_mh.insert(75)
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 100), (1, ': ', 99), (2, ': ', 75), (3, ': ', 58), (4, ': ', 72), (5, ': ', 61)]"
    )


def test_remove(get_mh):
    for i in [95, 75, 80, 55, 60, 50, 65]:
        get_mh.insert(i)
    get_mh.remove()
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 80), (1, ': ', 75), (2, ': ', 65), (3, ': ', 55), (4, ': ', 60), (5, ': ', 50)]"
    )
    get_mh.remove()
    assert (
        str(get_mh)
        == "mh:[(0, ': ', 75), (1, ': ', 60), (2, ': ', 65), (3, ': ', 55), (4, ': ', 50)]"
    )


#
# ## Leet Code style
#


def test_find_kth_smallest():
    """

    Heap: Kth Smallest Element in an Array

    You are given a list of numbers called nums and a number k.

    Your task is to write a function find_kth_smallest(nums, k) to find the kth smallest number in the list.

    The list can contain duplicate numbers and k is guaranteed to be within the range of the length of the list.


    """

    def find_kth_smallest(nums, k):
        max_heap = MaxHeap()

        for num in nums:
            max_heap.insert(num)
            if len(max_heap.heap) > k:
                max_heap.remove()

        return max_heap.remove()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert (find_kth_smallest(nums, k)) == 2

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_smallest(nums, k) == 3


def xx():
    """
        Heap: Maximum Element in a Stream

    Write a function named stream_max that takes as its input a list of integers (nums). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list
    """

    def stream_max(nums):
        max_heap = MaxHeap()
        max_stream = []

        for num in nums:
            max_heap.insert(num)
            max_stream.append(max_heap.heap[0])

        return max_stream

    nums = [1, 3, 2, 5, 4]
    assert stream_max(nums) == [1, 3, 3, 5, 5]
