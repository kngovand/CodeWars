def persistence(n):
    if n < 10:
        return 0
    else:
        return multiply(n, 0)


def multiply(number, total):
    added = 1
    str_n = str(number)

    if number >= 10:
        for num in str_n:
            added = added * int(num)
        return multiply(added, total + 1)

    elif number < 10:
        return total