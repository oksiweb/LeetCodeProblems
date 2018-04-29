def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    d = {}
    arr = []

    for i, el in enumerate(list1):
        if el in list2:
            d[el] = i + list2.index(el)
    value = min(d.values())
    for k in d.keys():
        if d[k] == value:
            arr.append(k)
    return arr

print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))