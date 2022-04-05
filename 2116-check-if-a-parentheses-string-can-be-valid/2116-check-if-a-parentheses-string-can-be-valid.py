class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        size, bal = len(s), 0
        if size % 2: return False
        for i in range(size):
            if s[i] == '(' or locked[i] == '0':
                bal += 1 
            else:
                bal -= 1
            if bal < 0:
                return False
        bal = 0
        for i in range(size - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return True