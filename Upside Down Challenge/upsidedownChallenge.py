def sameUpsidedown(number):
    i = 0
    maxIndex = len(number) - 1
    while i <= maxIndex:
        # print(number[i], number[maxIndex])
        if number[i] == "0" and number[maxIndex] != "0":
            return False
        elif number[i] == "6" and number[maxIndex] != "9":
            return False
        elif number[i] == "9" and number[maxIndex] != "6":
            return False
        elif number[i] != "6" and number[i] != "0" and number[i] != "9":
            print("Invalid String")
        i += 1
        maxIndex -= 1
    return True

print(sameUpsidedown("6090609"))
# output = true

print(sameUpsidedown("9669"))
# output = false
# Becomes 6996 when upside down.

print(sameUpsidedown("9"))
# output = false

print(sameUpsidedown("0"))
# output = true

print(sameUpsidedown("6090609"))
# output = true

print(sameUpsidedown("60906096090609"))
# output = true

print(sameUpsidedown("966909669"))
# output = false
# Becomes 699606699 when upside down.

print(sameUpsidedown("96666660999999"))
#output = false
