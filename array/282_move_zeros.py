def moveZeroes(nums):
    n = len(nums)
    for i,el in enumerate(nums):
        if i == n:
            break
        if el == 0:
            nums.remove(nums[i])
            nums.append(0)

nums = [3,0,3,0,4,3,5,0,4,0]
moveZeroes(nums)
print(nums)