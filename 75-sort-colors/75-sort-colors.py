class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = len(nums)
        for i in range(count):
            for j in range(1, count):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]

                