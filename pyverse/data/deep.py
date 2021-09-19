class deep(dict):
    """Like dict, allows to use prototype hierarchy, and access entries as attribute for get-obly mode. use methodes, with names starts with 'deep'"""
    def __init__(self, *args, **kwargs):
        super(deep, self).__init__(*args, **kwargs)
        self.proto = None # Property, thzat saves link to prototype object
    
    def __getattr__(self, name):
        return self.deepget(name)
    
    def deepget(self, name, *, depth:int = 0):
        if name in self:
            return self[name]
        elif self.proto == None:
            raise KeyError(f"No key '{name}' in object. Depth = {depth}")
        else:
            return self.proto.deepget(name, depth= depth + 1)
    
    def deephas(self, name):
        if name in self:
            return True
        elif self.proto == None:
            return False
        else:
            return self.proto.deephas(name)
    
    def deepfind(self, name):
        "Returns instance in hirerarchy, that has a key, passed as argument. Returns None if nothing found."
        if name in self:
            return self
        elif self.proto == None:
            return None
        else:
            return self.proto.deepfind(name)
    
    def deepset(self, name, value):
        "Allows to set value on key with actual key depth, or on depth 0 if key not found"
        if self.deephas(name):
            self.deepfind[name] = value
            return self
        self[name] = value
    
    def deepdel(self, name):
        "Allows to delete entry on key with actual key depth, or on depth 0 if key not found"
        if self.deephas(name):
            del self.deepfind(name)[name]
            return self
    
    def setprototype(self, proto):
        self.prototype = proto
        return self
    
    def fill(self, **kwargs):
        for key, value in kwargs.items():
            self.deepset(key, value)
        return self
    
    def up(self):
        return self.proto
    
    def upsafe(self):
        return self.proto if self.proto != None else self
    
    def hasprototype(self):
        return False if self.proto == None else True
    
    @classmethod
    def create(cls, proto=None, *origins, **kwargs):
        if not isinstance(proto, deep):
            raise TypeError("Only deep object can be uset as prototype for other deep objects.")
        return cls(*origins).setprototype(proto).fill(*kwargs)
