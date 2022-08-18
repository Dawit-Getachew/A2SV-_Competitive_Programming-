class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        while True:
            t = len(s)
            i = 0
            while i < len(s)-1:
                if s[i] != s[i+1] and (s[i] == s[i+1].lower() or s[i] == s[i+1].upper()):
                    s = s[:i] + s[i+2:]
                    continue
                i += 1
            if t == len(s):
                break
        return "".join(s)