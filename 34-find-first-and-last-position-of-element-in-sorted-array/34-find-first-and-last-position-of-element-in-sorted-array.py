class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, rightAns, leftAns = 0, len(nums)-1, -1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                rightAns = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif  nums[mid] > target:
                right = mid - 1
        left, right, leftAns = 0, len(nums)-1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                leftAns = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif  nums[mid] > target:
                right = mid - 1
        return [leftAns,rightAns]