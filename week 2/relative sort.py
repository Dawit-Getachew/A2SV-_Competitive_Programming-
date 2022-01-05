class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        identical=[]
        for i in arr2:
            for j in arr1:
                if j==i :
                    identical.append(j)
        difference=[]
        for i in arr1:
            if i not in arr2:
                difference.append(i)
        difference=sorted(difference)
        identical.extend(difference)
        return identical