class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        dic = {}
        for i, c in enumerate(s):
            if c in dic and start <= dic[c]:
                start = dic[c]+1
            else:
                res = max(res, i-start+1)
            dic[c] = i
        return res