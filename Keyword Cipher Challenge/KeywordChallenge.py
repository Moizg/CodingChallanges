# convert plaintext letter to position
# pick same position letter from cipher text
# add it to output string
def keyword_cipher(keyword, plaintext):
    alphabet_index = {chr(i + 96): i for i in range(1, 27)}
    cipher = ""
    ciphertext = generate_ciphertext(keyword)
    position = 0
    for i in range(len(plaintext)):
        position = alphabet_index[plaintext[i]]
        cipher = cipher + ciphertext[position-1]
    return cipher

def generate_ciphertext(key):
    ciphertext = key
    for i in range(1, 27):
        found = False
        for letters in key:
            if chr(i+96) == letters:
                found = True
                break
        if not found:
            ciphertext = ciphertext + chr(i+96)
    #print(ciphertext)
    return ciphertext


print(keyword_cipher("keyword", "abchij"))
#Output = "keyabc"

print(keyword_cipher("purplepineapple", "abc"))
#output = "pur"

print(keyword_cipher("mubashir", "edabit"))
#output = "samucq"

print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "abc"))
#Output = "eta"

print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "xyz"))
#Output = "qxz"

print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "aeiou"))
#Output = "eirfg"