best = -1
def binary_search(left, right, is_first):
nonlocal best
mid = left + (right-left)//2
if left > right:
return -1 if best==-1 else best
if nums[mid] > target:
return binary_search(left, mid-1, is_first)
elif nums[mid] < target:
return binary_search(mid + 1, right, is_first)
else:
if is_first:
right = mid -1
else:
left = mid + 1
best = mid
return binary_search(left, right, is_first)
left = 0
right = len(nums)-1
first_index = binary_search(left, right, True)
if first_index == -1:
return [-1 ,-1]
return [first_index, binary_search(left, right, False)]