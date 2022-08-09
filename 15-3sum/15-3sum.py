class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)
        nums.sort()
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            leftPointer = i + 1
            rightPointer = size - 1
            
            while leftPointer < rightPointer:
                Sum = nums[i] + nums[leftPointer] + nums[rightPointer]
                if Sum == 0:
                    res.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
                elif Sum < 0:
                    leftPointer += 1
                elif Sum > 0:
                    rightPointer -= 1
        return res