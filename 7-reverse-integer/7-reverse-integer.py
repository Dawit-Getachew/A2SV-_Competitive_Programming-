class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        res = "".join(reversed(str(abs(x))))
        return sign*int(res) if -2**31<=int(res)<=(2**31)-1 else 0