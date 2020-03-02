def is_substring(s1, s2):
    for char in s1:
        if char in s2:
            continue
        elif char not in s2:
            return False

    return True
