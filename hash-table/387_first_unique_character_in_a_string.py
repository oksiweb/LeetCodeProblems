def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    for el in s:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for i, el in enumerate(s):
        if d[el] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))