def disemvowel(string):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    new_str = string
    for x in string:
        if x in vowels:
            new_str = new_str.replace(x, '')
    return new_str