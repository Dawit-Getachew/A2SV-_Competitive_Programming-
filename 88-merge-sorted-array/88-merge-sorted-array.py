class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        if not m:
            nums1[:] = nums2[:]
        nums1[:] = sorted(nums1[:m] + nums2)