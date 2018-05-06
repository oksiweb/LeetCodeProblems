def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    arr = []

    for el in nums1:
        if el in nums2:
            arr.append(el)
            nums2.remove(el)
    return arr

print(intersect([1, 2, 2, 1], [2,2]))
