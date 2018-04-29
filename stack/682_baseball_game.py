def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    stack = []
    for el in ops:
        if el == "+":
            stack.append(stack[-1] + stack[-2])
        elif el == "D":
            stack.append(stack[-1] * 2)
        elif el == "C":
            stack.pop()
        else:
            stack.append(int(el))
    return sum(stack)

print(calPoints(["5","2","C","D","+"])) #30