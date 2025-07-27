from collections import Counter

def isValid(s):
    freq = Counter(s)
    freq_counts = Counter(freq.values())

    if len(freq_counts) == 1:
        return "YES"  # All characters have the same frequency

    if len(freq_counts) == 2:
        key1, key2 = freq_counts.keys()
        val1, val2 = freq_counts.values()

        # Case 1: One character occurs once, and its frequency is 1
        if (freq_counts[key1] == 1 and (key1 - 1 == key2 or key1 == 1)) or \
           (freq_counts[key2] == 1 and (key2 - 1 == key1 or key2 == 1)):
            return "YES"

    return "NO"
            
testCases = ["abc", "abcc", "aabbcd", "aabbccddeefghi", "abcdefghhgfedecba"]
for case in testCases:
    print(isValid(case))