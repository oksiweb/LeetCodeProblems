def arrayPairSum(nums):
    arr = sorted(nums)
    n = len(arr)
    i = 0
    sum = 0
    while i < n:
        sum += arr[i]
        i += 2
    return sum

print(arrayPairSum([1,4,3,2]))