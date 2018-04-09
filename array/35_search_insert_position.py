def searchInsert(nums, target):
    i = 0
    n = len(nums)
    while i < n:
        if target in nums:
            return nums.index(target)
        if nums[i] > target:
            return i
        i += 1
    return n

print(searchInsert([1,3,5,6], 5))