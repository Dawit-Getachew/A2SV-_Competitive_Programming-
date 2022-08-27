class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp not in mydict:
                mydict[tmp] = [s]

            else:
                mydict[tmp].append(s)

        return mydict.values()
