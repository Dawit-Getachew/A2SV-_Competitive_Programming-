class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for n in data:
            if n & 127 == n: #127 = 01111111
                if count: 
                    return False
                continue
            if n & 191 == n: #191 = 10111111
                if count: 
                    count -= 1
                    continue
                return False
            if count: 
                return False
            if n & 223 == n: #223 = 11011111
                count = 1

            elif n & 239 == n: #239 = 11101111
                count = 2
            elif n & 247 == n: #247 = 11110111
                count = 3
            else: #(n > 247) OR (n & 248 == 248) #248 = 11111000
                return False
        return count == 0