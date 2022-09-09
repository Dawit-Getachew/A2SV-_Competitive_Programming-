class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        count=maxe=0
        for a,d in properties:
            if d<maxe:
                count+=1
            maxe=max(maxe,d)
        return count