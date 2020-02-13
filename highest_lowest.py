def high_and_low(numbers):
    numbers = list(numbers.split(" "))
    numbers = list(map(int, numbers))

    numList = str(max(numbers)) + " " + str(min(numbers))
    return numList