def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    result = sum(map(int, list(str(num))))
    while result >= 10:
         result = sum(map(int, list(str(result))))
    return result


print(addDigits(199))