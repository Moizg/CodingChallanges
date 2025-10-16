## Keyword Cipher

A Keyword Cipher replaces each letter of a message with a letter from a shifted alphabet built using a keyword.

    Start with the keyword.

    Add the remaining letters of the alphabet (A–Z) in order, skipping any that already appeared in the keyword.

        Example keyword: "KEYWORD"

        Cipher alphabet: KEYWORDABCFGHIJLMNPQSTUVXZ

    Encrypt by replacing each letter in the message with the letter at the same position in the cipher alphabet.

        Plain alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

        Cipher alphabet: KEYWORDABCFGHIJLMNPQSTUVXZ

Write a function that takes a key and a message, and returns the encrypted message.
## Examples
```
keyword_cipher("keyword", "abchij")
Output = "keyabc"

keyword_cipher("purplepineapple", "abc")
output = "pur"

keyword_cipher("mubashir", "edabit")
output = "samucq"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "abc")
Output = "eta"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "xyz")
Output = "qxz"

keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "aeiou")
Output = "eirfg"
```