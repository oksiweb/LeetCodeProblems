def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for el in nums:
        if el in d:
            return el
        else:
            d[el] = 1

print(findDuplicate([3,4,2,3,3,7,8,9,2,3]))