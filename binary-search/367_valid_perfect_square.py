def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    start = 0
    end = num
    while start <= end:
        mid = (start + end) // 2
        if mid*mid == num:
            return True
        elif mid*mid > num:
            end = mid -1
        elif mid*mid < num:
            start = mid + 1
    return False

print(isPerfectSquare(16))