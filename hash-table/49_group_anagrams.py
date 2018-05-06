def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for el in strs:
        key = ''.join(sorted(el))
        if key in d:
            d[key].append(el)
        else:
            d[key] = [el]
    arr = []
    for el in d:
        arr.append(d[el])
    return arr

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))