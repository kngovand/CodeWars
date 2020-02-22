def namelist(names):
    result = []

    for name in names:
        result.append(name['name'])

    return (' & '.join(', '.join(result).rsplit(', ', 1)))