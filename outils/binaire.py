def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    while binary_number > 0:
        unity = binary_number % 10
        binary_number //= 10
        decimal_number += unity * (2 ** power)
        power += 1
    return decimal_number