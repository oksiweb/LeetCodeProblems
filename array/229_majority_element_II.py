def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    myset = set(nums)
    arr = []
    for el in myset:
        if nums.count(el) > len(nums)/3:
            arr.append(el)
    return arr



print(majorityElement([1,2,3,1,1,1,1]))