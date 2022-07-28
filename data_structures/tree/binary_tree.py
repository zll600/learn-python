class BinaryNode:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

    def substree_iter(A):
        if A.left:
            yield from A.left.subtree_iter()
        yield A
        if A.right:
            yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:
            return A.left.subtree_first()
        else:
            return A

    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        else:
            return A

    def successor(A):
        if A.right:
            return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:
            return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_insert_before(B)
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

class BinaryTree:
    def __init__(T, node_type = BinaryNode):
        T.root = None
        T.size = 0
        T.node_type = Node_Type

    def __len__(T):
        return T.size

    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

    def build(X):
        A = [x for x in X]
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.node_type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root

        self.root = build_subtree(A, 0, len(A) - 1)
