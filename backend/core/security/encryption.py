def encrypt(data, key):
    return "".join(chr(ord(c) + key) for c in data)

def decrypt(data, key):
    return "".join(chr(ord(c) - key) for c in data)
