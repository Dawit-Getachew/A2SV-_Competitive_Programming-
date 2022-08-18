class Solution:
    def isHappy(self, n: int) -> bool:
        n = list(str(n))
        seen = []
        total = 0
        while total != 1: 
            total = 0
            for i in range(len(n)):
                total += int(n[i]) ** 2
            n = list(str(total))
            if int(''.join(n)) == 1:
                return True
            else:
                if int(''.join(n)) in seen:
                    return False
                else:
                    seen.append(int(''.join(n)))