def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s_cut = s.split(' ')
    arr = []
    for el in s_cut:
        arr.append(el[::-1])
    r = ' '.join(arr)
    return r

print(reverseWords("Let's take LeetCode contest"))