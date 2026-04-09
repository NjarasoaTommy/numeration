def split_number(a):
    res = []
    while a > 0:
        res.append(a % 10)
        a //= 10
    res.reverse()
    return res

def element_addition(a, b):
    if a == b:
        return (1, 0) if a == 1 else (0, 0)
    else:
        return (0, 1)
        