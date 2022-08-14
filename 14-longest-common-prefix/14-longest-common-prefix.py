class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(min(strs,key = len)),0,-1):
            len1 = len(set(list(map(lambda x : x[:i],strs))))
            if len1 == 1:
                return strs[0][:i]
            
        return ''