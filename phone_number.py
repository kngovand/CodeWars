def create_phone_number(n):
    one = ""
    two = ""
    three = ""
    phone = ""

    for i in range(3):
        one += str(n[i])

    for i in range(3, 6):
        two += str(n[i])

    for i in range(6, 10):
        three += str(n[i])

    phone = "({0}) {1}-{2}".format(one, two, three)

    return phone