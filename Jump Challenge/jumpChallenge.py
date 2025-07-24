# my own approach
arr = [2,5,0,0]
arr1 = [2,3,1,1,4]
arr2 = [3,2,1,0,4]

def mapFunc(arr):
    maxJumps = {}

    for values in arr:
        jumps = []
        for i in range(1, values+1):
            jumps.append(i)
        maxJumps[values] = jumps
        
    print(maxJumps)
    return maxJumps

def canJump(arr):
    currentIndex = 0
    lastIndex = len(arr) - 1
    maxJumps = mapFunc(arr)
    
    for index in range(len(arr)):
        if index == 0 and arr[index] == 0: # if starting index value is 0 then you'll be stuck and hence return False
            break
        elif len(arr) == 1 and index == 0 and arr[index] == 0:
            return True
        elif len(arr) == 1 and index == 0 and arr[index] != 0:
            return True
        else:
            for value in maxJumps[arr[index]]:
                if arr[index] != 0 and (currentIndex + value) == lastIndex:
                    return True
        if arr[index] == 0 and index !=0:
            break
        currentIndex += 1
    return False

print("Jumping is:", canJump(arr))
print("Jumping is:", canJump(arr1))
print("Jumping is:", canJump(arr2))

# using gpt's help and the greedy approach

def canJump(arr) -> bool:
        reachable = 0
        for i, num in enumerate(arr):
            if i > reachable:
                return False
            reachable = max(reachable, i + num)
        return True