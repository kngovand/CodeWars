def unique_char(s):
    result = []

    for char in s:
        if char not in result:
            result.append(char)
        elif char in result:
            return False

    return True
