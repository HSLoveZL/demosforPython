print sorted([16, 32, 41, 23])


def reserved_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([16, 32, 41, 23], reserved_cmp)
