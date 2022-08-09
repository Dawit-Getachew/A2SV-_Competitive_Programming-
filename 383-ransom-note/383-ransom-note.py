class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = []
        rans[:0]=ransomNote
        mag = []
        mag[:0] = magazine
        countRans = Counter(rans)
        countMag = Counter(mag)
        for i in countRans:
            if countMag[i] >= countRans[i]:
                continue
            else:
                return False
        return True
        