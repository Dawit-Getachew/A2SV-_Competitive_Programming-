class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        great = []
        less = []
        equal = []
        for num in nums:
            if num > pivot:
                great.append(num)
            elif num < pivot:
                less.append(num)
            else:
                equal.append(num)
        return (less + equal + great)
            