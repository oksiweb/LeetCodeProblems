def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    i = 0
    while i < len(s):
        a = s[i:i+k]
        b = a[::-1]
        s = s.replace(a, b)
        i+=2*k
    return s

print(reverseStr("abcdefg", 2))