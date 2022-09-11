class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True, key=lambda x: x[0])
        speed_sum, result = 0, 0
        heap_engineers = []
        for count_efficiency, count_speed in engineers:
            if len(heap_engineers) >= k:
                speed_sum -= heap_engineers[0]
                heapq.heappop(heap_engineers)
            
            heapq.heappush(heap_engineers, count_speed)
            speed_sum += count_speed
            result = max(result, (speed_sum * count_efficiency))
            
        return result % ((10**9) + 7)