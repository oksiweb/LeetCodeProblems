def removeElement(nums, val):
    c = nums.count(val)
    i = 0
    while i < c:
        index = nums.index(val)
        nums.remove(nums[index])
        i = i + 1
    return len(nums)

print(removeElement([3,2,2,3], 3))