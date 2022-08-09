class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j=""
        for i in digits:
            j +=str(i)
        return list(str(int(j) + 1))