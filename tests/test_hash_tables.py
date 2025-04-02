def test_ds(get_ht):
    assert set(["set_item", "keys"]).issubset(get_ht.ds_func)


def test_constrcutor(get_ht):
    assert get_ht.get_id == "hash-table"
    assert (
        str(get_ht)
        == "ht:[(0, ': ', None), (1, ': ', None), (2, ': ', None), (3, ': ', None), (4, ': ', None), (5, ': ', None), (6, ': ', None)]"
    )


def test_ht(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)
    get_ht.set_item("lumber", 70)
    assert (
        str(get_ht)
        == "ht:[(0, ': ', None), (1, ': ', None), (2, ': ', None), (3, ': ', None), (4, ': ', [['bolts', 1400], ['washers', 50]]), (5, ': ', None), (6, ': ', [['lumber', 70]])]"
    )


def test_set_item(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)
    assert "1400" == str(get_ht.get_item("bolts"))
    assert "50" == str(get_ht.get_item("washers"))
    assert "None" == str(get_ht.get_item("lumber"))


def test_keys(get_ht):
    get_ht.set_item("bolts", 1400)
    get_ht.set_item("washers", 50)
    get_ht.set_item("lumber", 70)
    assert str(get_ht.keys()) == "['bolts', 'washers', 'lumber']"


def test_find_duplicates():
    """
    HT: Find Duplicates ( ** Interview Question)"

    "find_duplicates()"

    "Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary)."


    """

    def find_duplicates(l):
        entries = {}
        c = []
        for item in l:
            if entries.get(item):
                c.append(item)
            entries[item] = True
        return list(set(c))

    assert find_duplicates([1, 2, 3, 4, 5]) == []
    assert find_duplicates([1, 1, 2, 2, 3]) == [1, 2]
    assert find_duplicates([1, 1, 1, 1, 1]) == [1]
    print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
    print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([]))


def test_first_non_repeating_char():
    """
    "HT: First Non-Repeating Character ( ** Interview Question)"

    "You have been given a string of lowercase letters."

    "Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None."
    """

    def first_non_repeating_char(txt):
        d = {}
        for c in txt:
            if d.get(c) is None:
                d[c] = 0
            else:
                d[c] += 1
        for k, v in d.items():
            if v == 0:
                return k
        return None

    assert first_non_repeating_char("leetcode") == "l"
    assert first_non_repeating_char("hello") == "h"
    assert first_non_repeating_char("aabbcc") is None


def test_group_anagrams():
    """

    HT: Group Anagrams ( ** Interview Question)"

    "You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams."

    """

    def group_anagrams(l):
        d = {}
        for item in l:
            sorted_item = "".join(sorted(item))
            if d.get(sorted_item) is None:
                d[sorted_item] = []
            d[sorted_item].append(item)

        return [*d.values()]

    print("1st set:")
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]

    print("2nd set:")
    assert group_anagrams(["abc", "cba", "bac", "foo", "bar"]) == [
        ["abc", "cba", "bac"],
        ["foo"],
        ["bar"],
    ]

    print("3rd set:")
    assert group_anagrams(
        ["listen", "silent", "triangle", "integral", "garden", "ranged"]
    ) == [["listen", "silent"], ["triangle", "integral"], ["garden", "ranged"]]


def test_two_sum():
    """

    HT: Two Sum ( ** Interview Question)"

    "Problem:"
    "Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target."


    """

    def two_sum(nums, target):
        num_map = {}
        for k, v in enumerate(nums):
            num_map[v] = k
        print(num_map)
        for k, v in enumerate(nums):
            complement_to_target = target - v
            if num_map.get(complement_to_target):
                return [k, num_map[complement_to_target]]
        return []

    assert two_sum([5, 1, 7, 2, 9, 3], 10) == [1, 4]
    assert two_sum([4, 2, 11, 7, 6, 3], 9) == [1, 3]
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    print(two_sum([1, 3, 5, 7, 9], 10))
    print(two_sum([1, 2, 3, 4, 5], 10))
    print(two_sum([1, 2, 3, 4, 5], 7))
    print(two_sum([1, 2, 3, 4, 5], 3))
    print(two_sum([], 0))


def test_subarray_sum():

    def subarray_sum(nums, target):
        sum_map = {0: -1}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            if current_sum - target in sum_map:
                return [sum_map[current_sum - target] + 1, i]
            sum_map[current_sum] = i
        return []

    nums = [1, 2, 3, 4, 5]
    target = 9
    assert subarray_sum(nums, target) == [1, 3]
    print(subarray_sum(nums, target))  # should print [1, 3]


def test_remove_duplicates():
    """

    "Set: Remove Duplicates ( ** Interview Question)"

    "You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list."

    "You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates."

    "Your function should not modify the original list, instead, it should create a new list with unique values and return it."

    """


def remove_duplicates(l):
    return list(set(l))


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
assert new_list == ([1, 2, 3, 4, 5, 6, 7, 8, 9])


# ---


def test_has_unique_chars():
    """

    Set: Has Unique Chars ( ** Interview Question)"

    "Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise. "


    """

    def has_unique_chars(a_string):
        char_set = set()
        for char in a_string:
            if char in char_set:
                return False
            char_set.add(char)
        return True

    assert has_unique_chars("abcdefg")  # should return True
    assert (has_unique_chars("hello")) is False  # should return False


def test_find_pairs():
    """
        Set: Find Pairs ( ** Interview Question)

    You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
    """

    def find_pairs(arr1, arr2, target):
        set1 = set(arr1)
        return [
            (complement, num)
            for num in arr2
            for complement in [target - num]
            if complement in set1
        ]

    # """
    #     def find_pairs(arr1, arr2, target):
    #         set1 = set(arr1)
    #         pairs = []
    #         for num in arr2:
    #             complement = target - num
    #             if complement in set1:
    #                 pairs.append((complement, num))
    #         return pairs
    # """
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    target = 7

    assert find_pairs(arr1, arr2, target) == [(5, 2), (3, 4), (1, 6)]

    arr1 = [1, 2, 3, 5]
    arr2 = [1, 3, 4, 5]
    target = 11

    assert find_pairs(arr1, arr2, target) == []


def test_longest():
    """
        Set: Longest Consecutive Sequence ( ** Interview Question)

    Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
    """

    def longest_consecutive_sequence(nums):
        num_set = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
