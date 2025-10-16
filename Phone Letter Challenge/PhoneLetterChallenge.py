def letterCombinations(number):
    phone_mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                     "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    outputList = []
    if not number:
        return outputList

    # collect only mapped strings; ignore digits like '1' or '0'
    keyValuePair = [phone_mapping[d] for d in number if d in phone_mapping]
    if not keyValuePair:
        return outputList

    # start with an empty prefix and build up
    outputList = [""]
    for chars in keyValuePair:
        new_list = []
        for prefix in outputList:
            for ch in chars:
                new_list.append(prefix + ch)
        outputList = new_list

    return outputList


# Tests
print(letterCombinations("23"))   # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))     # []
print(letterCombinations("2"))    # ["a","b","c"]
print(letterCombinations("234"))  # combinations of 'abc' x 'def' x 'ghi'
print(letterCombinations("27"))   # combinations of 'abc' x 'pqrs'
print(letterCombinations("79"))   # combinations of 'pqrs' x 'wxyz'