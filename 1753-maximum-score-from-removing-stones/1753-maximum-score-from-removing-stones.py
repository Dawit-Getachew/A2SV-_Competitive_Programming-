class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = [a,b,c]
        stones.sort()
        score = 0
        while True:
            stones[-1] -= 1
            stones[-2] -= 1
            stones.sort()
            zeroCount = 0
            for i in range(len(stones)):
                if stones[i] == 0:
                    zeroCount += 1
            score += 1
            if zeroCount >= 2:
                break
        return score
            