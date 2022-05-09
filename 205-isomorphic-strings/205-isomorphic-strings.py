class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHash, tHash = {}, {}
        for iS, jT in zip(s,t):
            if (iS in sHash and sHash[iS] != jT) or (jT in tHash and tHash[jT] != iS):
                return False
            sHash[iS] = jT
            tHash[jT] = iS
        return True