def dominantIndex(nums):
    mn = 0
    index = 0
    for i, el in enumerate(nums):
        if el > mn:
            mn = el
            index = i
    for el in nums:
        if el == mn:
            continue
        if mn < 2*el:
            return -1
    return index

print(dominantIndex([3, 6, 1, 0]))