def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] == target and nums[right] == target:
            return [left, right]
        elif nums[left] < target:
            left +=1
        else:
            right -=1

    return [-1, -1]

print(searchRange([5,7,7,8,8,10], 8))