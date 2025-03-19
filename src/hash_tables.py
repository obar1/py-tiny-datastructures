from typing import List

from src.a_ds import ADS


class HashTable(ADS):
    @property
    def get_id(self):
        return "hash-table"

    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print(self):
        for i, val in enumerate(self.data_map):
            yield (i, ": ", val)

    def __repr__(self):
        return f"ht:{list(self.print())}"

    def set_item(self, k, v):
        guid = self.__hash(k)
        if self.data_map[guid] is None:
            self.data_map[guid] = []
        self.data_map[guid].append([k, v])
        return True

    def get_item(self, key):
        index = self.__hash(key)
        try:
            tmp: List = self.data_map[index]
            assert tmp or tmp == []
            for k in tmp:
                if k[0] == key:
                    return k[1]
        except AssertionError:
            return None
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
