def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    if s == '':
        return True
    s = re.findall(r"\w+",s)
    s = ''.join(s).lower()
    i = 0
    n = len(s) - 1
    while i <= n:
        if s[i] == s[n-i]:
            i += 1
            continue
        else:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))