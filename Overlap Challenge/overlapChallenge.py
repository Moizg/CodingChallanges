def Overlap(word1, word2):
    max_overlap = 0
    maxLength = min(len(word1), len(word2))
    
    for i in range(1, maxLength + 1):
        if word1[-i:] == word2[:i]:
            max_overlap = i  # keep checking for longer overlap
    
    return word1 + word2[max_overlap:]
          
testCases = [("sweden","denmark"), ("honey", "milk"), ("dodge", "dodge"), ("level", "level"), ("sad", "das")]        
for w1, w2 in testCases:
    print(f"Overlap({w1}, {w2}) → {Overlap(w1, w2)}")
