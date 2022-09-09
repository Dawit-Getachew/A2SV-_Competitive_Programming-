class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        n = len(A)
        for c in A: c.sort()

        g = [set() for _ in range(n)]  # a->b means a<=b
        din = [0] * n  # in_degree
        for i in range(n):
            for j in range(n):
                if i != j and all(di <= dj for di, dj in zip(A[i], A[j])) and i not in g[j]:
                    g[i].add(j)
                    din[j] += 1

        hmx = [h for _, _, h in A]  # max heights

        que = collections.deque([i for i in range(n) if din[i] == 0])
        while que:  # topological sort
            p = que.popleft()
            for q in g[p]:
                hmx[q] = max(hmx[q], hmx[p] + A[q][2])
                din[q] -= 1
                if din[q] == 0: que.append(q)
        return max(hmx)