def convert_to_title(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("number must be an integer >= 1")

    rev = []
    while number > 0:
        number -= 1                 # adjust so 0..25 maps to A..Z
        rem = number % 26
        rev.append(chr(ord('A') + rem))
        number //= 26

    # reverse before returning
    return ''.join(reversed(rev))

print(convert_to_title(1))
#output = "A"
print(convert_to_title(18))
#output = "R"
print(convert_to_title(28))
#output = "AB"
print(convert_to_title(52))
#output = "AZ"
print(convert_to_title(701))
#output = "ZY"
print(convert_to_title(229704))
#output = "MATT"
print(convert_to_title(209380622941))
#output = "ZATOICHI"