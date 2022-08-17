class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(list(s))):
            return len(s)
        count = 0
        Set = list()
        for i in s:
            if i not in Set:
                Set.append(i)
                count = max(count, len(Set))
            else:
                while i in Set:
                    Set = Set[1:]
                count = max(count, len(Set))
                Set.append(i)
        return count