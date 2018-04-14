def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    arr = []
    for el in nums1:
        if el not in arr and el in nums1 and el in nums2:
            arr.append(el)
    return arr

print(intersection([1, 2, 2, 1], [2,2]))