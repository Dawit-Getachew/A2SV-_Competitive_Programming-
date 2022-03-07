def cookies(k, A):
    # Write your code here
    noOfIteration = 0
    size = len(A)
    h.heapify(A)
    while A[0] < k and size >= 2:
        tempOne = h.heappop(A)
        tempTwo = h.heappop(A)
        h.heappush(A, 1 * tempOne + 2 * tempTwo)
        noOfIteration += 1
        size = len(A)
    res = noOfIteration if A[0] >= k else -1
    return res
