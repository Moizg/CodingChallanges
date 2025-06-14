def next_letters(alphabet):
    if alphabet == "":
        return "A"
    
    # FIRST WE GET THE LAST LETTER FROM THE STRING 
    lastLetter = alphabet[-1:]
    print(f"The last letter is {lastLetter}")
    
    # CONVERTING IT TO ITS ASCII VALUE
    lastLetterASCII = ord(lastLetter)
    
    if lastLetterASCII >= 65 and lastLetterASCII <= 89:
        lastLetterASCII += 1
        # CONCATENATE AND RETURN THE STRING
        return alphabet[:len(alphabet)-1] + chr(lastLetterASCII) 
    elif lastLetterASCII == 90:
        if len(alphabet) == 1: # IF "Z" IS THE INPUT STRING THEN SIMPLY RETURN "AA"
            return "AA"
        else:
            """ IF THE LAST LETTER IS A Z AND THE LENGTH OF THE STRING IS MORE THAN 1, MEANING THERE 
            ARE MORE LETTERS i-e CAZ, THEN RECURSIVELY CALL THE FUNCTION ON THE STRING BEHIND Z AND CONCATENATE
            THE RESULT WITH A TO GET FINAL OUTPUT
            e.g input = "CAZ" 
                recursive call on "CA" which will return "CB" 
                output = "CB" + "A" """
            return next_letters(alphabet[:len(alphabet)-1]) + "A"
    
test_cases = ["", "A", "ABY", "Z", "FBIZ"]
i = 1 
for test in test_cases:
    print(f"TEST CASE {i}:")
    i += 1
    print("Input =", test)
    print("Output =", next_letters(test))
    
""" alphabet = input("Enter your letter/s in capital:")
print("Input string =", alphabet)

# CALL FUNCTION AND STORE THE NEW INCREMENTED OUTPUT
nextLetter = next_letters(alphabet)

print(f"The next letter/s = {nextLetter}") """