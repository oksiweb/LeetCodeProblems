def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    stack = []
    for el in nums:
        if len(stack) != 0:
            p = stack.pop()
            if el != p:
                stack.append(p)
        else:
            stack.append(el)
    return stack[-1]


print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))