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

    if __name__ == "__main__" :
        ciphertext = input("Enter Atbash cipher text: ")
        plaintext = atbash_decrypt(ciphertext)
        print("\nDecrypt massage: ")
        print(plaintext)