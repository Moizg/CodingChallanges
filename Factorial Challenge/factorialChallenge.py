"""
First we define a normal recursive factorial function that calculates and returns the factorial of any positive integer.
Then we calculate the factorial of factorials by calling factorial for each number in fact_of_fact.
"""

def factorial(integer):
    if integer == 0:
        return 1
    else:
        return integer * factorial(integer - 1)

def fact_of_fact(integer):
    i = 0
    output = 1
    while i <= integer:
        output = output * factorial(i)
        i += 1
    return output

number = input("Enter number to find factorial of factoraials of:")
print(f"The factorial of factorials of {number} is {fact_of_fact(int(number))}")