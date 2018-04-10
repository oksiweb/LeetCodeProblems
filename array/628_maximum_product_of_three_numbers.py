def maximumProduct(nums):
    nums = sorted(nums)
    two_negative_and_one_positive = nums[0] * nums[1] * nums[len(nums) - 1]
    three_positive = nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3];
    return max(two_negative_and_one_positive, three_positive)


print(maximumProduct([-9, -12, -3, -8, 2, 6]))
print(maximumProduct([-3,-1,-1,0,1,2,3]))