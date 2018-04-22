def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myset = set(nums)
    for el in myset:
        if nums.count(el) >= len(nums)/2:
            return el

print(majorityElement([1,2,3,4,5,1,1,1,1]))

