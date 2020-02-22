def rot13(message):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in message:
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                if (0 <= i < 13) or (26 <= i < 39):
                    integer = i + 13
                elif (13 <= i < 26) or (39 <= i < 52):
                    integer = i - 13
                result += alphabet[integer]
        if char not in alphabet:
            result += char
                #result.append(alphabet[integer])
    return result