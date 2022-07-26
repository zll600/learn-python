def direct_access_sort(A):
    """ 
    Sort A assuming items have distinct non-negative keys
    """
    u = 1 + max([x.key for x in A]) 
    D = [None] * u 
    for x in A:
        D[x.key] = x 
    i = 0 
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1
