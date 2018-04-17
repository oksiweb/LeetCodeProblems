def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i,el in enumerate(nums):
        d[el] = i

    for i, el in enumerate(nums):
        second = target - nums[i]
        if second in d and d[second] != i:
            return [i, d[second]]


print(twoSum([2, 7, 11, 15], 9))