def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    while binary_number > 0:
        unity = binary_number % 10
        binary_number //= 10
        decimal_number += unity * (2 ** power)
        power += 1
    return decimal_number

def decimal_to_binary(decimal_number):
    if decimal_number == 2:
        return 10
    elif decimal_number < 2:
        return decimal_number
    binary_number = decimal_number % 2
    power = 1
    decimal_number //= 2
    is_zero = False
    while decimal_number >= 2:
        unity = decimal_number % 2        
        binary_number = binary_number + \
            (unity * (10 ** power) if unity != 0 else 10 ** (power + (1 if unity == 0 else 0))) - \
            (10 ** power if is_zero else 0)
        is_zero = True if unity == 0 else False
        decimal_number //= 2
        power += 1
    binary_number = binary_number + decimal_number * (10 ** power) - (10 ** power if is_zero else 0)

    return binary_number