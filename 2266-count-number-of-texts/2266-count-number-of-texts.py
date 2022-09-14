class Solution:
    def countTexts(self, K: str) -> int:
        m = [1]
        for p, k in zip('.'+K, K):
            del m[:-(k!=p or 3+(k in '79'))]
            m += sum(m) % 1000000007,
        return m[-1]