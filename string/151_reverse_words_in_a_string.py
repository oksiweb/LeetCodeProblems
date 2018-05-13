def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    if s.strip() == '':
        return ''

    arr = s.strip().split(' ')
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

    r = []
    for el in arr:
        if el != '':
            r.append(el)

    return ' '.join(r)


print(reverseWords("the sky is blue"))