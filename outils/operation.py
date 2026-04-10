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
        
def join_number(a):
    res = a[0]
    for x in a[1:]:
        res = (res * 10 if res != 0 else 10) + x
    return res

def addition(a, b):
    x = split_number(a)
    y = split_number(b)
    if len(x) > len(y):
        max = x
        min = y
    else:
        max = y
        min = x
    res = [0 for _ in min]
    r = 0
    for i, _ in enumerate(min):
        r, u = element_addition(r, x[-1 - i])
        old_r = r
        is_first_r = True if r != 0 else False
        r, res[len(min) - i - 1] = element_addition(y[-1 - i], u)
        r += old_r if is_first_r else 0

    remaining_size = len(max) - len(min)
    for i in range(remaining_size):
        x = max[remaining_size - 1 - i]
        r, u = element_addition(r, x)
        res = [u, *res]
    if r != 0:
        res = [r, *res]

    return join_number(res)