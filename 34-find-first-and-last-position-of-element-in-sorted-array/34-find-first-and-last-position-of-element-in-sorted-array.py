class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, True), self.search(nums, target, False)]
    def search(self, nums, target, first):
        left = 0
        right = len(nums)-1
        ans = -1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                ans = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return ans
                