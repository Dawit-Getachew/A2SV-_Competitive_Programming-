class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)
        for i in s:
            hashMapS[i] += 1
        for i in t:
            hashMapT[i] += 1
        for i in hashMapS:
            if hashMapS[i] == hashMapT[i]:
                continue
            else:
                return False
        for i in hashMapT:
            if hashMapS[i] == hashMapT[i]:
                continue
            else:
                return False
        return True
            