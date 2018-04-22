def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word.isupper():
        return True

    if word[0].isupper() or not word[0].isupper():
        for el in word[1:]:
            if el.isupper():
                return False
        return True
    return False

print(detectCapitalUse("FlaG"))