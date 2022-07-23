from typing import Any

from array.array import Array

class SortedArraySet:
    def __init__(self):
        self.A = Array()

    def __len__(self):
        return len(self.A)

    def __iter__(self) -> Any:
        yield from self.A

    def iter_order(self) -> Any:
        yield from self.A

    def build(self, X: List[Any]):
        self.A.build(X)
        self._sort()

    def _binary_search(self, k: Any, i: int, j: int) -> int:
        if i >= j:
            return i

        m = (i + j) // 2
        x = self.A.get_at(m)

        if x.key > k:
            return self._binary_search(k, i, m - 1)
        if x.key < k:
            return self._binary_search(k, m + 1, j)

        return m

    def find_min(self) -> Any:
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self) -> Any:
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def find(self, k) -> Any:
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k:
            return x
        else:
            return None

    def prev_next(self, k: int) -> Any:
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0,len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k:
            return x
        if i + 1 < len(self):
            return self.A.get_at(i + 1)
        else:
            return None

    def find_prev(self, k: int) -> Any:
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k:
            return x
        if i > 0:
            return self.A.get_at(i - 1)
        else:
            return None

    def insert(self, x: Any):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self) - 1)
            k = self.A.get_at(i)
            if k == x.key:
                self.A.set_at(i, x)
                return False
            if k > x.key:
                self.A.insert_at(i, x)
            else:
                self.A.insert_at(i + 1, x)
        return True


