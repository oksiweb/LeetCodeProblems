def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    arr = []
    for el in range(1, n+1):
        if el % 15 == 0:
            arr.append("FizzBuzz")
        elif el % 3 == 0:
            arr.append("Fizz")
        elif el % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(str(el))
    return arr

print(fizzBuzz(15))