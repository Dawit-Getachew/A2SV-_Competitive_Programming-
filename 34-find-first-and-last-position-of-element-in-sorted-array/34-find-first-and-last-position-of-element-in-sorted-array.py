class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        seen = -1
        def binarySearch(left, right, seenDir: bool):
            nonlocal seen
            if left > right:
                return seen
            mid = left + (right-left)//2
            if nums[mid] > target:
                return binarySearch(left, mid-1, seenDir)
            elif nums[mid] < target:
                return binarySearch(mid+1, right, seenDir)
            else:
                if seenDir:
                    right = mid - 1
                else:
                    left = mid + 1
                seen = mid
            return binarySearch(left, right, seenDir)
        left, right = 0, len(nums)-1
        binarySearch(left, right, True)        
        return [seen, binarySearch(left, right, False)]
                    