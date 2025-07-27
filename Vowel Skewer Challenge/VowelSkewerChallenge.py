import re

def is_authentic_skewer(skewer):
    if not skewer or all(c == '-' for c in skewer):
        return False
    
    
    skewer_count = re.findall(r'[A-Z](-+)[A-Z]', skewer)
    if len(set(skewer_count)) != 1:
        return False
    
    skewer_pattern = skewer_count[0]
    skewer_split = skewer.split(skewer_pattern)
    
    vowels = set("AEIOU")
    if skewer_split[0] in vowels or skewer_split[-1] in vowels:
        return False
    
    for i, ch in enumerate(skewer_split):
        if (i % 2 == 0 and ch in vowels) or (i % 2 == 1 and ch not in vowels):
            return False
            
    return True
    
test_cases = ["HELLO",
              "B--A--N--A--N--A--S", 
              "A--X--E", 
              "C-L-A-P", 
              "M--A---T-E-S"]
for cases in test_cases:
    print(is_authentic_skewer(cases))