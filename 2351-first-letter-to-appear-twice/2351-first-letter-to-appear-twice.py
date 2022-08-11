class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # hashMap = defaultdict(int)
        # for i in s:
        #     hashMap[i] += 1
        #     if hashMap[i] == 2:
        #         return i

        Set = set()
        for i in s:
            if i in Set: return i
            Set.add(i)