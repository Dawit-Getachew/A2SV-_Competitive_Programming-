class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans=[]
        hmap={}
        idx=0
        for w in words:
            hmap[w[::-1]]=idx
            idx+=1
        for i, word in enumerate(words):
            if word in hmap and hmap[word]!=i:
                ans.append([i,hmap[word]])            
            if word!="" and "" in hmap and word==word[::-1]:
                ans.append([i,hmap[""]])
                ans.append([hmap[""],i])
            for k in range(len(word)):
                if word[k:] in hmap and word[:k]==word[k-1::-1]:
                    ans.append([hmap[word[k:]],i])
                if word[:k] in hmap and word[k:]==word[:k-1:-1]:
                    ans.append([i, hmap[word[:k]]])
        return ans