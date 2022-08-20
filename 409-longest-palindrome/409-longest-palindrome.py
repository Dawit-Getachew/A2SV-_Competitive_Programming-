class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        res = 0
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            if count[char] == 2:
                res += 2
                count.pop(char)
        return res if len(count.keys()) == 0 else res + 1
    
    