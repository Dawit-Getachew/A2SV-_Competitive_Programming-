class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        val = start ^ goal
        count = bin(val).count("1")
        return count