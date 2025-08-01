def atbash_decrypt(ciphertext):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                result += chr(ord('z') - (ord(char) - ord('a')))
            else :
                result += chr(ord('Z') - (ord(char) - ord('A')))
        else :
            result += char
    
    return result