class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        pairs = list(zip(efficiency, speed))
        pairs = sorted(pairs, reverse=True)
        topk = []  
        topk_sum = 0
        max_perform = 0
        for eff, sp in pairs:
            max_perform = max(max_perform, eff * (topk_sum + sp))

            if len(topk) < k - 1 or (topk and sp > topk[0]):
                topk_sum += sp
                heappush(topk, sp)
                if len(topk) > k - 1:
                    topk_sum -= heappop(topk)
        return max_perform % (10**9 + 7)