import heapq as h
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countedWords = Counter(words)
        priorityWord = [(-countedWords[word], word) for word in countedWords]
        h.heapify(priorityWord)
        res = [h.heappop(priorityWord)[1] for _ in range(k)]
        return res
        
