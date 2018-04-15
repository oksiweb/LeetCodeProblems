# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    start = 0
    end = n
    while start <= end:
        mid = (start+end)//2
        r = guess(mid)
        if r == 0:
            return mid
        elif r == 1:
            start = mid + 1
        elif r == -1:
            end = mid -1
    return -1