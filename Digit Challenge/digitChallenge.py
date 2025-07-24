def digits(string):
    nums = 0
    for letter in cString:
        nums += 1
    return nums

number = int(input("Enter any number:"))
cString = ""

for n in range(1, number, 1):
    cString = cString + str(n)
    
print(digits(cString))

