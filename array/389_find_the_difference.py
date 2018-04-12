def findTheDifference(s, t):
    arr = list(s)
    for el in t:
        if el in arr:
            arr.remove(el)
        else:
            return el


print(findTheDifference("abcd", "abcde"))