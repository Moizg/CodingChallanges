def evalAlgebra(equation):
    tokens = equation.split(" ")
    # Find '=' position
    eq_index = tokens.index("=")
    left = tokens[:eq_index]
    right = tokens[eq_index + 1:]
    
    # Convert right-hand side to integer
    rhs = int(right[0])
    
    # Handle the left-hand side
    if left[0] == "x":
        # x + num = rhs
        op = left[1]
        num = int(left[2])
        if op == "+":
            return rhs - num
        elif op == "-":
            return rhs + num
            
    elif left[1] == "+":
        num = int(left[0])
        if left[2] == "x":
            return rhs - num
        
    elif left[1] == "-":
        num = int(left[0])
        if left[2] == "x":
            return num - rhs
        

# Test cases
print(evalAlgebra("2 + x = 19"))     # 17
print(evalAlgebra("4 - x = 1"))      # 3
print(evalAlgebra("x + 10 = 53"))    # 43
print(evalAlgebra("-23 + x = -20"))  # 3
print(evalAlgebra("10 + x = 5"))     # -5
print(evalAlgebra("-49 - x = -180")) # 131
print(evalAlgebra("x - 22 = -56"))   # -34
