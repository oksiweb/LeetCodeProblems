def selfDividingNumbers(left, right):
    arr = []
    i = left
    while i <= right:
        if i < 10:
            arr.append(i)
            i += 1
            continue
        s = str(i)
        t = 1
        for el in s:
            if int(el) != 0 and i % int(el) == 0:
                continue
            else:
                t = 0
        if t == 1:
            arr.append(i)
        i += 1
    return arr

print(selfDividingNumbers(1,22))