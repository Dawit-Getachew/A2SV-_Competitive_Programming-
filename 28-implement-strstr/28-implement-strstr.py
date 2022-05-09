class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        
        # if not needle:
        #     return 0
        # haystackList = list(haystack)
        # needleList = list(needle)
        # for i in range(len(haystackList)):
        #     if "".join(haystackList[i:i+len(needle)]) == needle:
        #         return i
        # return -1