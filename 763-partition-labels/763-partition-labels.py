class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        chrPos = {}
        for index, char in enumerate(S):      
            chrPos[char] = index
        left, right = 0, 0
        result = []
        for index, char in enumerate(S):
            right = max(right, chrPos[char])
            if right == index:
                result.append(right - left + 1)
                left = index + 1
        return result