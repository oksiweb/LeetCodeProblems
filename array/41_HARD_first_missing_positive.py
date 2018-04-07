def firstMissingPositive(nums):
    i = 1
    n = len(nums)
    num = 0
    while i<= n:
        if i in nums:
            num = i
            i += 1
            continue
        else:
            return i
        i += 1
    return num + 1

print(firstMissingPositive([3,4,-1,1]))  #2