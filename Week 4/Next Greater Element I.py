class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterMap = {}
        stack = []
        for num in nums2:  # O(n)
            while stack and stack[-1] < num:
                greaterMap[stack.pop()] = num
            stack.append(num)
        
        return [greaterMap.get(num, -1) for num in nums1] # O(n)