def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    myset = set(nums)

    i = 1
    arr = []
    while i < len(nums):
        if i not in myset:
            arr.append(i)
        i += 1
    return arr

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))