class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            Sum = count = 0
            for w in weights:
                if (Sum + w) > mid:
                    count += 1
                    Sum = 0
                Sum += w
            if Sum > 0:
                count += 1
            return count
        
        left, right = max(weights), sum(weights)
        while left <= right:
            mid =  left + (right - left)//2
            if check(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    