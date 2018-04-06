def containsDuplicate(nums):
    d = {}
    for el in nums:
        if el in d:
            return True
        else:
            d[el] = 1
    return False

print(containsDuplicate([1,2,3,2]))