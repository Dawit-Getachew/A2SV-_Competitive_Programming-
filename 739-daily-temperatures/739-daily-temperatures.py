class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, stack = len(temperatures), []
        result = [0] * n
        for i in reversed(range(n)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result