class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = Counter(arr)
        distinctN = len(freqs)
        sortedFreqs = [(k,v) for k,v in sorted(freqs.items(), key=lambda item: item[1])]
        toRemove = k
        removed = 0
        while toRemove > 0:
            toRemove -= sortedFreqs[removed][1]
            removed += 1
        if toRemove < 0: removed -= 1       
        return distinctN - removed