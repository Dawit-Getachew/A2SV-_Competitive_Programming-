class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(filter(lambda num: num%2 == 0, nums))
        res = []
        for val, idx in queries:
            if not nums[idx] % 2:
                even_sum -= nums[idx]
            nums[idx] += val
            if not nums[idx] % 2:
                even_sum += nums[idx]            
            res.append(even_sum)            
        return res