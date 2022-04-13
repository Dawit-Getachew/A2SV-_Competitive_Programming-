class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        if not points or points == [[]]:
            return 0
        points.sort(key=lambda x: x[1])
        shot = points[0][1]
        numArrow = 1
        for balloon in points:
            if balloon[0] > shot:
                numArrow += 1
                shot = balloon[1]
        return numArrow