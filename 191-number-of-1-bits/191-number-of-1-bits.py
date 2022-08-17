class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ""
        for i in range(32):
            res += '1' if n&(1<<i) else '0'
        return res.count('1') 