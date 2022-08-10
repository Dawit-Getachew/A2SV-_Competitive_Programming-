import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = string.punctuation
        s = list(''.join([i.lower() for i in s if not i in punc if i != ' ']).strip())
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
            
        return True