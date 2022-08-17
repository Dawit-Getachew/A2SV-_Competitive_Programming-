class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        flag = False
        for i in range(len(nums)):
            if nums[i] in dic:
                flag = True if abs(dic[nums[i]] - i) <= k else False
                dic[nums[i]] = i
                if flag == True:
                    return True
            else:
                dic[nums[i]] = i
        return False