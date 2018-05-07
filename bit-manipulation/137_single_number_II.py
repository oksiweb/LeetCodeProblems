def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for el in nums:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1

    for el in nums:
        if d[el] == 1:
            return el

print(singleNumber([0,1,0,1,0,1,99]))