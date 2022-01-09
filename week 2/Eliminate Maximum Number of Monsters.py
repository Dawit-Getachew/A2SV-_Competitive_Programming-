class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(math.ceil(dist[i]/speed[i]))
        time.sort()
        for i in range(0, len(time)):
            if time[i]<=i:
                return i
        return len(dist)