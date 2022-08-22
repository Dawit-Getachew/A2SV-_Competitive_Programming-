class Solution:
    def firstUniqChar(self, s: str) -> int:
        for key,count in Counter(s).items():
            if count == 1:
                return s.index(key)
        return -1