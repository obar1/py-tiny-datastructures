from src.a_ds import ADS


class Graph(ADS):
    @property
    def get_id(self):
        return "graph"

    # pylint: disable=C0201,C0206

    def __init__(self):
        self.adj_list = {}

    def print(self):
        for vertex in self.adj_list:
            yield f"{vertex}:{self.adj_list[vertex]}"

    def __repr__(self):
        return f"g:{list(self.print())}"

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        try:
            assert all(item in self.adj_list.keys() for item in [v1, v2])
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        except AssertionError:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for ov in self.adj_list[vertex]:
                self.adj_list[ov].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
