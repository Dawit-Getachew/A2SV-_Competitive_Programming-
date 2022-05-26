class Solution:
    def reverseBits(self, n: int) -> int:
        result, bit = 0, 31
        while n:
            result += (n & 1) << bit
            n >>= 1
            bit -= 1
        return result