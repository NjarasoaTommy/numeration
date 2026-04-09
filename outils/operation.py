def split_number(a):
    res = []
    while a > 0:
        res.append(a % 10)
        a //= 10
    res.reverse()
    return res