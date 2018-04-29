def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    d_open = {
       '(': 1,
       '{': 2,
       '[': 3
    }

    d_closed = {
        ')' : 1,
        '}': 2,
        ']': 3
    }

    stack = []
    for el_1 in s:
        if el_1 in d_open:
            stack.append(el_1)
        else:
            if len(stack) == 0:
                return False
            el_2 = stack.pop()
            if d_open[el_2] != d_closed[el_1]:
                return False
    if len(stack) == 0:
        return True
    return False


print(isValid("()[]{}"))