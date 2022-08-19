class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right, duplicate = 0, len(nums) - 1, 0
        while left <= right:
            mid = left + (right - left)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        return duplicate
        