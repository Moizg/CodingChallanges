def findBrokenKeys(inputPhrase, testPhrase):
    brokenKeys = []
    for words1, words2 in zip(inputPhrase, testPhrase):
        for letter1, letter2 in zip(words1, words2):
            if letter1 != letter2:
                if letter1 not in brokenKeys:
                    brokenKeys.append(letter1)
    
    return brokenKeys

inputPhrase = input("Enter typed phrase:")
testPhrase = input("Enter test phrase:")

brokenKeys = findBrokenKeys(inputPhrase, testPhrase)

if not brokenKeys:
    print("No broken keys")
else:
    print(f"The broken keys are {brokenKeys}") 