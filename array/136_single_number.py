def singleNumber(nums):
    d = {}
    for el in nums:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
            r = el
    return min(d, key=d.get)

print(singleNumber([3,4,4,2,2,3,1]))