class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in timePoints:
            times.append( int(timePoint.split(":")[0])*60 +int(timePoint.split(":")[1]))
        for i in range(len(times)):
            if times[i] == 0:
                times[i] = 24*60
        times.sort()
        minimum = min(times[-1] - times[0], 1440 - times[-1] + times[0])
        print(times)
        for i in range(len(times)-1):
            minimum = min(minimum, times[i+1] - times[i], 1440 + times[i] - times[i+1])
        return minimum