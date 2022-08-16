class Solution:
    def longestPalindrome(self, s: str) -> str:
        def judge(s:str, left: int, right: int, tmp_s) -> str:
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp_s = s[left] + tmp_s + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            return tmp_s
        result_s = ''
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                # case 1
                tmp_s = judge(s, i - 2, i + 1, s[i] + s[i - 1])
                if len(tmp_s) > len(result_s):
                    result_s = tmp_s
            # case 2
            tmp_s = judge(s, i - 1, i + 1, s[i])
            if len(tmp_s) > len(result_s):
                result_s = tmp_s
        return result_s


    