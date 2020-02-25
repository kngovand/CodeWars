def string_compression(s):
    str = list(s)
    count = 0
    for x in range(len(str)):
        while str[x] == str[x+1]:
            count+=1
            print(count)
        str[x+1] = str(count)
        count = 0

    return str