class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = collections.defaultdict(list)
        res = []
        for word in strs:
            w = "".join(sorted(word))
            if w in check:
                check[w].append(word)
            else:
                check[w] = [word]
        return [val for val in check.values()]
