class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [(int(time.split(":")[0])*60 + int(time.split(":")[1])) for time in timePoints]
        for i in range(len(times)):
            if times[i] == 0:
                times[i] = 24*60
        times.sort()
        minimum = min(times[-1] - times[0], 1440 - times[-1] + times[0])
        print(times)
        for i in range(len(times)-1):
            minimum = min(minimum, times[i+1] - times[i])
        return minimum