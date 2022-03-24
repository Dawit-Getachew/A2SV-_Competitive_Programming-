class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charPosition, result = {}, []
        left, right = 0, 0
        for index, char in enumerate(S):      
            charPosition[char] = index
        for index, char in enumerate(S):
            right = max(right, charPosition[char])
            if right == index:
                result.append(right - left + 1)
                left = index + 1
        return result