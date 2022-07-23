from typing import Any, List

class Array:
    def __init__(self):
        """
        create a fix size  array
        >>> array = Array()
        """
        self.A = []
        self.size = 0

    def __len__(self):
        """
        return length of array eg. number of elements
        >>> array = Array()
        >>> len(array)
        0
        """
        return self.size
    
    def __iter__(self):
        """
        return the stored items one-by-one in sequence order
        >>> array = Array()
        """
        yield from self.A

    def build(self, X: Any):
        """
        given an iterable X, build sequence from items in X
        >>> array = Array()
        >>> array.build([1, 2, 3, 4])
        """
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i: int) -> Any:
        """
        return the ith item
        >>> array = Array()
        """
        return self.A[i]

    def set_at(self, i: int, x: Any):
        """
        replace the ith item with x
        >>> array = Array()
        """
        self.A[i] = x

    def _copy_forward(self, i: int, n: int, A: List[Any], j: int):
        # copy n items from self.A start at i to A start at j
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i: int, n: int, A: List[Any], j: int):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i: int, x: Any):
        """
        add x as the ith item
        """
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - 1, A, i + 1)
        self.build(A)
        
    def delete_at(self, i: int):
        """
        remove and return the ith item
        """
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i) 
        self.build(A)
        return x

    def insert_first(self, x):
        """
        add x as the first item
        """
        self.insert_at(0, x)

    def delete_first(self):
        """
        remove and return the first item
        """
        return self.delete_at(0)

    def insert_last(self, x):
        """
        add x as the last item
        """
        return insert_at(len(self), x)

    def insert_last(self, x):
        """
        add x as the last item
        """
        self.insert_at(len(self) - 1);

if __name__ == '__main__':
    import doctest

    doctest.testmod()
