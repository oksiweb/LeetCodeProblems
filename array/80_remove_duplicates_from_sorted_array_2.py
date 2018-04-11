def removeDuplicates(nums):
    d = {}
    i = 0
    while i < len(nums):
        if nums[i] in d:
            d[nums[i]] += 1
            if d[nums[i]] > 2:
                nums.remove(nums[i])
                continue
        else:
            d[nums[i]] = 1
        i += 1

    return len(nums)

print(removeDuplicates([1,1,1,2,2,3]))