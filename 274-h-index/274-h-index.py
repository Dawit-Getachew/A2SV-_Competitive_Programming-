class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        for i, ct in enumerate(citations):
            if i >= ct:
                return i
        return len(citations)