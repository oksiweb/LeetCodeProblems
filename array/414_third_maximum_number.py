def thirdMax(arr):
    max1 = max2 = max3 = 0
    nums = set(arr)
    for el in nums:
        if el >= max1 or max1 == 0:
            max3 = max2
            max2 = max1
            max1 = el
            continue
        elif el >= max2 or max2 == 0:
            max3 = max2
            max2 = el
            continue
        elif el >= max3 or max3 == 0:
            max3 = el
            continue
    if len(nums) < 3:
        return max1
    else:
        return max3

print(thirdMax([1,2,3])) // 1
print(thirdMax([2,3,4,1])) // 2
