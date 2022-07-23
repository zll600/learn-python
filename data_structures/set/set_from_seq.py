from typing import Any

class SetFromSeq:
    def __init__(self):
        self.S = None

    def __len__(self):
        return len(self.S)

    def __iter__(self):
        yield from self.S

    def build(self, A):
        """
        given an iterable X, build set from items in X
        """
        self.S.build(A)

    def insert(self, x):
        """
        add x to set(replace item with key x.key if key already exist)
        """
        for i in range(len(self.S)):
            if self.S.get_at(i).key == x.key:
                self.S.set_at(i, x)
                return

        self.S.insert_last(x)

    def delete(self, k):
        """
        remove and return the stored item with key k
        """
        for i in range(len(self)):
            if self.S.get_at(i).key == k:
                return self.S.delete_at(i)

    def find(self, k):
        """
        return the stored item with key x
        """
        for x in self:
            if x.key == k:
                return x
        return None

    def find_min(self):
        """
        return teh stored data smallest key
        """
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    def find_max(self):
        """
        return the stored item with largest key
        """
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    def find_next(self):
        """
        return the stored item with smallest key smallest larger than k
        """
        out = None
        for x in self:
            if x.key > k:
                if x.key > k:
                    if (out is None) or (x.key < out.key):
                        out = x
            return out

    def find_prev(self, k):
        """
        return the stored item with largest key larget than k
        """
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_ord(self):
        """
        return the stored items one-by-one in key order
        """
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)
    
