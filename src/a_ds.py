from abc import ABC


class ADS(ABC):
    @property
    def get_id(self):
        return "id"

    @property
    def ds_func(self):
        return set(self.__class__.__dict__)
