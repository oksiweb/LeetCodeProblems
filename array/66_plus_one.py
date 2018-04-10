def plusOne(digits):
    first_el = digits[0]
    n = len(digits)
    if n > 1 or first_el+1 == 10:
        n_str = int(''.join(map(str, digits))) + 1
        return list(map(int, str(n_str)))
    else:
        digits[0] += 1
    return digits

print(plusOne([9,9]))