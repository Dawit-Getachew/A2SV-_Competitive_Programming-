class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
                if nums[start] == target:
                    return start
                start += 1
        return -1