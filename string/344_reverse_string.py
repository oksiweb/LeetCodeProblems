def reverseString(s):
    """
    :type s: str
    :rtype: str
    """

    start = 0
    end = len(s) - 1
    arr = list(s)

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return ''.join(arr)

print(reverseString("hello"))