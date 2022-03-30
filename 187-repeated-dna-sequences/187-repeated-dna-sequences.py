class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10:
            return []
        subStr, result = set(), set()
        for i in range(len(s)-9):
            if s[i:i+10] in subStr:
                result.add(s[i:i+10])
            else:
                subStr.add(s[i:i+10])
        return list(result)