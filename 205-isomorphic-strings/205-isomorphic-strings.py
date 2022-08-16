class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        
        for i in range(len(s)):
            if (s[i] in dict):
                if (dict[s[i]] != t[i]):
                    return False
            else:
                if (t[i] in dict.values()):
                    return False
                else:
                    dict[s[i]] = t[i]
                    
        return True