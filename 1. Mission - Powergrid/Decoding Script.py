encryptedCode = "'/+=)8iig"
key = [0x57,0x58,0x59,0x5a,0x5b,0x5c,0x5d,0x5e,0x5f]

for index, keyElement in enumerate(key):
    print(chr(keyElement ^ ord(encryptedCode[index])), end='')