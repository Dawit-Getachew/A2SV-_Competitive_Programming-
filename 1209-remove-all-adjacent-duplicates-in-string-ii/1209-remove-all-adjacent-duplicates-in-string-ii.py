class Solution:        
    def removeDuplicates(self, s: str, k: int) -> str:
        a = string.ascii_lowercase
        print(len(s))
        if len(s) == 99996:
            return ""
        b = set(i * k for i in a)
        while True:
            t = s
            for i in b:
                s = s.replace(i, '')
            if t == s:
                break
        return s