class NodeP:
    """Node with next and prev"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return f"node:{self.value}"
