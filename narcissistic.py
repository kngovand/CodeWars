def narcissistic(value):
    total = 0
    new_value = str(value)

    for i in new_value:
        exponent = int(i) ** len(new_value)
        total += exponent

    if total == value:
        return True
    else:
        return False