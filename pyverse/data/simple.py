__all__ = ["loop", "scope"]

from pyverse.core import basis

class loop(list, basis):
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
    

class scope(dict, basis):
    "Actualy dict, but extended wit attribute-like access. Iterating by default equivalent to dict.items(). Allows to find value by index «.(index: int)»"

    def __call__(self, index: int):
        return self.getByIndex(index)
    
    def getByIndex(self, index: int):
        return tuple(self.values())[index]
    
    def getKeyByIndex(self, index: int):
        return tuple(self.keys())[index]
    
    def __iter__(self):
        return self.items()
    
    def __getattr__(self, name):
        return self[name]
    
    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        super().__setattr__(name, value)
    
    def getDynamic(self, key):
        "if value is callable, returns result of calling it function or method, with scope instance as first arg."
        if callable(self[key]):
            return self[key](self)
        return self[key]


