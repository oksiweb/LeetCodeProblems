def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n = len(needle)

    if needle == '':
        return 0

    for i, el in enumerate(haystack):
        if el == needle[0]:
            if haystack[i:i+n] == needle:
                return i
    return -1