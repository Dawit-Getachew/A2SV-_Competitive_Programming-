class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aInt, bInt = int(a,2), int(b,2)        
        while bInt:
            answer = aInt ^ bInt
            carry = (aInt & bInt) << 1
            aInt, bInt = answer, carry 
        return bin(aInt)[2:]
    