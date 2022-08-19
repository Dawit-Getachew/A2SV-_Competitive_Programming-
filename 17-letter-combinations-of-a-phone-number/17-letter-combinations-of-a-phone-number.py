class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map_dict = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        } 
        if len(digits) == 1:
            return map_dict[digits]
       
        c_s = map_dict[digits[0]]
        res = []
        for i in c_s:
            res += [i+j for j in self.letterCombinations(digits[1:])]
        return res