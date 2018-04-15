def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    start = 0
    end = x
    while start <= end:
        mid = (start + end) / 2
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            end = mid - 1
        elif mid*mid < x:
            start = mid + 1
    return end


print(mySqrt(4))