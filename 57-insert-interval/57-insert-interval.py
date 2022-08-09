class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []    
        (start, end) = newInterval
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                left.append(intervals[i])
            elif intervals[i][0] <= newInterval[1]:
                start = min(intervals[i][0],start)
                end = max(intervals[i][1], end)
            else:
                right.append(intervals[i])
        return left + [[start,end]] + right
        