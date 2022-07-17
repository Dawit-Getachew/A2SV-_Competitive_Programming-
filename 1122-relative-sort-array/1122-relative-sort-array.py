class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        unique = []
        hashMap = dict().fromkeys(arr2,0)
        for i in range(len(arr1)):
            if arr1[i] in hashMap.keys():
                hashMap[arr1[i]] += 1
            else:
                unique.append(arr1[i])
        ans = []
        for i in range(len(arr2)):
            temp = [arr2[i]] * hashMap[arr2[i]]
            ans.extend(temp)
        ans.extend(sorted(unique))
        return ans