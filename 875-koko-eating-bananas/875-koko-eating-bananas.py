class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        left, right, k = 1, max(piles), float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for p in piles:
                if mid >= p:
                    count += 1
                else:
                    count += math.ceil(p/mid)
            if count <= h:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1
        return k