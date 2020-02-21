def increment_string(strng):
    value = ''
    string = ''
    trailing_zero = 0

    for char in strng:
        if char.isdigit() and char == '0':
            trailing_zero += 1
        elif char.isdigit() and char != '0':
            value += char
        else:
            string += char

    if not value:
        value = int(1)
    else:
        value = int(value) + 1

    string = string + '{0:0{width}}'.format(value, width=trailing_zero)

    return string