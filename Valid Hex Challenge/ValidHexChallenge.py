def is_valid_hex(hexcode):
    if len(hexcode) == 7 and hexcode[0:1] == "#":
        hexcode = hexcode[1:]
        hexcode = hexcode.lower()
        #print(hexcode)
        for letters in hexcode:
            if (ord(letters) >= 48 and ord(letters) <=57) or (ord(letters) >= 97 and ord(letters) <=102):
                continue
            else:
                print("False, invalid character")
                return
        print("True")
    else:
        print("False, length exceeded or # missing")

is_valid_hex("#CD5C5C")
is_valid_hex("#EAECEE")
is_valid_hex("#eaecee")
is_valid_hex("#CD5C58C")
is_valid_hex("#CD5C5Z")
is_valid_hex("#CD5C&C")
is_valid_hex("CD5C5C")