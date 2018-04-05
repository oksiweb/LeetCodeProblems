def removeDuplicates(nums):
    i = 0
    d = {}
    while i < len(nums):
        if nums[i] not in d:
            d[nums[i]] = 1
            i += 1
        else:
            nums.remove(nums[i])
    return nums

print(removeDuplicates([1,2,2,1,2,4,5]))