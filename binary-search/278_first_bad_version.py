def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start = 0
    end = n

    while start < end:
        mid = (start + end) // 2

        if isBadVersion(mid) == True:
            end = mid
        elif isBadVersion(mid) == False:
            start = mid + 1

    return start