class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        finalList = []
        for i in intervals:
            if not finalList or finalList[-1][1]<i[0]:
                finalList.append(i)
            else:
                finalList[-1][1]=finalList[-1][1] if finalList[-1][1] > i[1] else i[1]
        return finalList
