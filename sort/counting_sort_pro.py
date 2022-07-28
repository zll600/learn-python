def counting_sort(A):
    """
    Sort A assuming items have non-negative keys
    """
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
        D[x.key] += 1
    for k in range(1, u):
        D[k] += D[k - 1]
    for x in list(reversed(A)):
        A[D[x.key] - 1] = x
        D[x.key] -= 1
