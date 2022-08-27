class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        height, width = len(matrix), len(matrix[0])
        res = -inf
        for top_row in range(height):
            nums = [0] * width
            for bottom_row in range(top_row, height):
                for colnum in range(width):
                    nums[colnum] += matrix[bottom_row][colnum]
                prefixsums_encountered = [0]
                prefixsum = 0
                for pos, num in enumerate(nums, 1):
                    prefixsum += num
                    complement = prefixsum - k
                    complement_pos = bisect_left(prefixsums_encountered, complement)
                    if complement_pos < pos:
                        subarray_sum = prefixsum - prefixsums_encountered[complement_pos]
                        if subarray_sum == k:
                            return k
                        elif subarray_sum < k:
                            res = max(res, subarray_sum)
                    insort(prefixsums_encountered, prefixsum)
        return res