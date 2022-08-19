class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        res = []
        for n in nums1:
            if n in table: 
                table[n] += 1
            else: 
                table[n] = 1
        for n in nums2:
            if n in table and table[n] > 0:
                res.append(n)
                table[n] -= 1
        return res