def permutation(x, y):
    str1 = list(x)
    str2 = list(y)

    if len(x) != len(y):
        return False

    for char in str1:
        if char in str2:
            str2.remove(char)

    if not str2:
        return True
    else:
        return False
