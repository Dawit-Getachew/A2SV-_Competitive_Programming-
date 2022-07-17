class Solution:
    def sortSentence(self, s: str) -> str:
        lis = s.split()
        res = [0]* len(lis)
        for i in range(len(lis)):
            temp = []
            temp = list(lis[i])
            # temp[:0] = lis[i]
            num = -1
            num = int(temp[-1])
            temp.pop()
            temp = ''.join(temp)
            res[num-1] = temp
        return ' '.join(res)
            