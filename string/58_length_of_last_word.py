def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    arr = s.strip().split(" ")
    n = len(arr)
    if n > 0:
        return len(arr[n-1])
    else:
        return 0

print(lengthOfLastWord("Hello World"))