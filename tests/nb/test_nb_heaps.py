import sys, os

sys.path.append(os.path.abspath(".."))


from src.heaps import MaxHeap


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
