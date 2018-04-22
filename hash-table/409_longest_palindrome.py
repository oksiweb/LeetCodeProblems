def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    counter = 0
    for el in s:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for key, value in d.items():
        if value / 2 >= 1:
            counter += value // 2 * 2

    if counter < len(s):
        return counter + 1
    return counter

print(longestPalindrome("abccccdd"))