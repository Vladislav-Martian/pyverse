from pyverse.core import basis

class dcell(basis):
    """Stores data, and leads it inside pipeline.
    """
    def __init__(self, o=None, meta={}):
        self.inbox = o.inbox if isinstance(o, self.getClass()) else o
        self.meta = meta
        self.stopped: bool = False

    def __getitem__(self, name):
        return self.meta[name]

    def __setitem__(self, name, value):
        self.meta[name] = value

    def __delitem__(self, name):
        del self.meta[name]

    def __contains__(self, name):
        return self.meta.__contains__(name)

    def get(self, name, default=None):
        try:
            return self.meta[name]
        except (KeyError, NameError, IndexError, AttributeError):
            return default

    def __getattr__(self, name):
        return getattr(self.inbox, name)
    
    def clearmeta(self):
        self.meta.clear()

    def setval(self, value):
        self.inbox = value
        return self
    
    def __iter__(self):
        return self.meta.items()
    
    def stop(self):
        self.stopped = True
        return self
    
    def unstop(self):
        self.stopped = False
        return self
    
    def isStopped(self):
        return self.stopped
