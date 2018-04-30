def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = []
    d = {}
    for el in nums:
        if el in d:
            d[el] += 1
            arr.remove(el)
        else:
            d[el] = 1
            arr.append(el)
    return arr

print(singleNumber([1, 2, 1, 3, 2, 5])) #[3,5]