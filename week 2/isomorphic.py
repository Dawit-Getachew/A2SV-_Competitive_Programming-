class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphicS = dict()
        isomorphicT= dict()
        for a, b  in zip(s, t):
            if ((a in isomorphicS and isomorphicS[a] != b) or (b in isomorphicT and isomorphicT[b] != a)):
                return False
            isomorphicS[a] = b
            isomorphicT[b] = a    
        return True