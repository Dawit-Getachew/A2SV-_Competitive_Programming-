import heapq as h
class MedianFinder:

    def __init__(self):
        self.rightHalf = []
        self.leftHalf = []

    def addNum(self, num: int) -> None:
        if len(self.leftHalf) > len(self.rightHalf):
            temp = h.heappush(self.leftHalf, -num)
            temp2 = h.heappop(self.leftHalf)
            h.heappush(self.rightHalf, -temp2)
        else:
            temp = h.heappush(self.rightHalf, num)
            temp2 = h.heappop(self.rightHalf)
            h.heappush(self.leftHalf, -temp2)
    def findMedian(self) -> float:
        if len(self.leftHalf) == len(self.rightHalf):
            temp = (-self.leftHalf[0] + self.rightHalf[0])/2
            return temp
        else:
            return -self.leftHalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()