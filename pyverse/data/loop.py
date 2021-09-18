class loop(list):
    "List, but works with indexes in a different way. Works as looped list. Iterations in cycle ar finite."

    def __getitem__(self, index):
        index = index % len(self)
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        index = index % len(self)
        return super().__setitem__(index, value)

    def __delitem__(self, index):
        index = index % len(self)
        return super().__delitem__(index)

    def insert(self, index, object):
        index = index % len(self)
        return super().insert(index, object)

    def pop(self, index):
        index = index % len(self)
        return super().pop(index)

    def first(self, index: int = 0):
        return self[index]

    def last(self, index: int = 0):
        return self[len(self) - index - 1]
