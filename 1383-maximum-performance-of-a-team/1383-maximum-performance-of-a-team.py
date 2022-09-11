class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        sorted_engineers_by_efficiency = sorted(zip(efficiency, speed), reverse=True)
        max_performance = 0
        sum_of_speed = 0
        the_highest_speed_engineers = []
        
        for engineer_efficiency, engineer_speed in sorted_engineers_by_efficiency:
            heapq.heappush(the_highest_speed_engineers, engineer_speed)
            sum_of_speed += engineer_speed

            if len(the_highest_speed_engineers) > k:
                sum_of_speed -= heapq.heappop(the_highest_speed_engineers)

            performance = sum_of_speed * engineer_efficiency
            if performance > max_performance:
                max_performance = performance

        return max_performance % (10**9+7)