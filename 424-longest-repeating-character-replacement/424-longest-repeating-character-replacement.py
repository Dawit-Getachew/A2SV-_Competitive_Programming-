class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        i, j= 0, 0
        MaxChar, ans= 0, -1
        pair = [0]*26
        while j<len(s):
            pair[ord(s[j])-65] += 1
            MaxChar=max(MaxChar, pair[ord(s[j])-65])
            currLen = j-i+1
            if currLen-MaxChar>k:
                pair[ord(s[i])-65] -= 1
                i += 1
            currLen=j-i+1
            ans=max(ans,currLen)
            j += 1 
        return ans
        