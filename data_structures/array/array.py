from typing import Any

class ArraySeq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size
    
    def __iter__(self):
        yield from self.A

    def build(self, X: Any):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i: int) -> Any:
        return self.A[i]

    def set_at(self, i: int, x: Any):
        self.A[i] = x

    def _copy_forward(self, i: int, n: int, A: List, j: int):
        # copy n items from self.A start at i to A start at j
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i: int, n: int, A: List, j: int):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i: int, x: Any):
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - 1, A, i + 1)
        self.build(A)
        
    def delete_at(self, i: int):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i) 
        self.build(A)
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        return insert_at(len(self), x)

    def insert_last(self, x):
        self.insert_at(len(self) - 1);

