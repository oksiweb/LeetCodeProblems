def pivotIndex(nums):
    S = sum(nums)
    n = len(nums)
    i = 0
    left_sum = 0
    while i < n:
        if left_sum == S - left_sum - nums[i]:
            return i
        left_sum += nums[i]
        i += 1
    return -1

print(pivotIndex([1, 7, 3, 6, 5, 6]))