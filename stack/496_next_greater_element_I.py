def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """

    arr = []

    for el in findNums:
        i = nums.index(el) + 1
        while i < len(nums):
            if nums[i] > el:
                arr.append(nums[i])
                break
            i += 1
        if i >= len(nums):
            arr.append(-1)

    return arr

print(nextGreaterElement([4,1,2], [1,3,4,2]))