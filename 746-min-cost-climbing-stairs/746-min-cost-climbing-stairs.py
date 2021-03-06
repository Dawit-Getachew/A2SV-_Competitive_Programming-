class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        pre = 0
        curr = 0
        for cost in costs:
            pre, curr = curr, cost + min(curr,min(pre,curr))
        return min(pre, curr)