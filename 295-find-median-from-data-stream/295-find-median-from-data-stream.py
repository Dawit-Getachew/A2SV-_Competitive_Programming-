import heapq as h
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self,num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            self.arr.sort()
            i = n//2
            return (self.arr[i] + self.arr[i-1])/2
            # temp = []
            # for _ in range((len(self.arr)//2 + 1)):
            #     temp.append(h.heappop(self.arr))
            # res1 = (temp[-1] + temp[-2])/2  
        else:
            self.arr.sort()
            return self.arr[n//2]
            return
#             temp =[]
#             for _ in range((len(self.arr)//2 + 1)):
#                 temp.append(h.heappop(self.arr))
        
#             res = temp[-1]
#             return res
        return 0
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()