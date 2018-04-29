def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d_s = {}
    d_t = {}

    for el in s:
        if el in d_s:
            d_s[el] += 1
        else:
            d_s[el] = 1

    for el in t:
        if el in d_t:
            d_t[el] += 1
        else:
            d_t[el] = 1

    return d_s == d_t

print(isAnagram("anagram", "nagaram"))