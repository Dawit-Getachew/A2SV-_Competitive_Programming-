from heapq import heappush as hpush, heappop as hpop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        heap = []
        res = 0
        total_spd = 0
        min_efe = math.inf
        for efe, spd in sorted(zip(efficiency, speed), reverse=True):
            total_spd += spd
            min_efe = min(min_efe, efe)
            hpush(heap, spd)
            if len(heap) > k:
                total_spd -= hpop(heap)
            res = max(res, total_spd * min_efe)
        return res % MOD