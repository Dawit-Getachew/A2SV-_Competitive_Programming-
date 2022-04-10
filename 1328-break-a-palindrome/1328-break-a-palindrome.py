class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        change =  False
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)//2):
            if(palindrome[i]=='a'):
                continue
            else:
                palindrome= palindrome[:i] + "a" + palindrome[i+1:]
                change = True
                break
        if(change):
            return palindrome
        else: 
            palindrome = palindrome[:len(palindrome)-1] + "b"
            return palindrome