'''
Uses 'string'.count() method to determine index
'''

def string_compression(s):
    result = ""
    chars = list(s)
    index = 0

    while index < len(chars):
        char = chars[index]
        count = s.count(char)

        result += char + str(count)
        index += count

    return result