class Solution:
    def fib(self, n: int) -> int:
        visited = {}
        def helper(n):
            if n < 2:
                return n
            if n not in visited:
                visited[n] = helper(n-1) + helper(n-2)
            return visited[n]
        return helper(n)