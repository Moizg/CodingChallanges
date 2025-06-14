def actualMemorySize(memorySize):
    sizeInt = int(memorySize[0:len(memorySize)-2]) # slicing and seperating the integer part of the size
    sizeStr = memorySize[-2:]                 # slicing and seperating the string (GB, MB, KB, etc) part of the size
    print(f"The memory size is {sizeInt} {sizeStr}")
    
    match sizeStr:
        case "GB":
            actualSize = sizeInt - (0.07*sizeInt)
        case "MB":
            sizeInt = sizeInt/1000 # convert to GB
            # this way we can easily implement the check i-e actualSize < 1
            actualSize = sizeInt - (0.07*sizeInt)
    
    if sizeStr == "GB" and sizeInt > 1:
        return f"{actualSize:.4g}", "GB"
    if actualSize < 1:
        return int(actualSize*1000), "MB"

# main
memorySize = input("Enter the size of your USB or memory storage: ")

# call function with memory size as arguement
actualSize, sizeStr = actualMemorySize(memorySize)
print(f"The actual size is {actualSize} {sizeStr}")