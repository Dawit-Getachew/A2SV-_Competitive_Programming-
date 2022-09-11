class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        profits, vp = [], []

        ps = [1000] + prices + [0]
        for v, p in pairwise(b for a, b, c in zip(ps, ps[1:], ps[2:]) if (a < b) ^ (b < c)):
            while vp and (v < vp[-1][0] or p >= vp[-1][1]):
                pv, pp = vp.pop()
                if pv <= v:
                    v, pv = pv, v
                if pp > pv:
                    profits.append(pp - pv)
            vp.append((v, p))
        else:
            profits.extend(p - v for v, p in vp)

        return sum(nlargest(k, profits))