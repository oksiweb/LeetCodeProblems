def findDuplicates(nums):
    d = {}
    r = []
    for el in nums:
        if el in d:
            r.append(el)
        else:
            d[el] = 1
    return r



print(findDuplicates([4,3,2,7,8,2,3,1]))