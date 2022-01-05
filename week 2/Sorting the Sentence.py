class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s.sort(key = lambda x: x[-1])
        sent=""
        for i in s:
            sent += (i[:-1]+" ")
        sent.strip()
        return sent