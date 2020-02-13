def find_outlier(integers):
    isEven = 0
    isOdd = 0
    number = 0

    for i in integers:
        if i % 2 == 0:
            isEven += 1
        elif i % 2 != 0:
            isOdd += 1

    if isEven == 1:
        for i in integers:
            if i % 2 == 0:
                number = i
    elif isOdd == 1:
        for i in integers:
            if i % 2 != 0:
                number = i

    return number