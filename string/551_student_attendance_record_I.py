def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    l = 0
    a = 0
    for i,el in enumerate(s):
        if el == 'L':
            l += 1
        elif el == 'P':
            l = 0
        elif el == 'A':
            a += 1
            l = 0
        if a > 1 or l > 2:
            return False
    return True

print(checkRecord("PPALLP"))