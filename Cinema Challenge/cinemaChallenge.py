def maxSeating(arr):
    found = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            continue
        
        # check neighbors safely
        backone  = arr[i-1] if i-1 >= 0 else 0
        backtwo  = arr[i-2] if i-2 >= 0 else 0
        frontone = arr[i+1] if i+1 < len(arr) else 0
        fronttwo = arr[i+2] if i+2 < len(arr) else 0
        
        if backone == backtwo == frontone == fronttwo == 0:
            arr[i] = 1
            found += 1
    return found

arr = [0,0,0,1,0,0,1,0,0,0]
print(f"There are {maxSeating(arr)} seats available.")
arr = [1, 0, 0, 0, 0, 1]
print(f"There are {maxSeating(arr)} seats available.")
arr = [0,0,0,0]
print(f"There are {maxSeating(arr)} seats available.")
