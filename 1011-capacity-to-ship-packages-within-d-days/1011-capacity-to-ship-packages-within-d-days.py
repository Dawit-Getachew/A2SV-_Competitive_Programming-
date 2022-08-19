class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            Sum, count = 0, 0
            for w in weights:
                Sum += w
                if Sum <= mid:
                    continue
                else:
                    count += 1
                    Sum = w
            if Sum > 0:
                count += 1
            return count <= days
        
        left, right = max(weights), sum(weights)
        while left <= right:
            mid =  left + (right - left)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    