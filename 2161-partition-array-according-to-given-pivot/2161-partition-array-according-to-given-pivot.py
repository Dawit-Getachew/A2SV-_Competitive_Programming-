class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        great = []
        small = []
        equal = []
        for num in nums:
            if num > pivot:
                great.append(num)
            elif num < pivot:
                small.append(num)
            else:
                equal.append(num)
        return (small + equal + great)
            