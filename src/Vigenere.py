# Author:        Aleaddin Ozer
# Descripton:    Vigenere implementation in Python
# Lisence:       Use it where ever you want but it always be mine

key = input("What is the key: ")

#ask user for encryption or decryption
def getChoose():
    choose = input("Now what is your intention?\n" + "Enter e for encryption or d for decryption: ")
    if choose.upper() == 'E':
        plain_text = input("Enter plain text: ")
        print("Encrypted as:", encryption(plain_text, key))
        print("Encrypted text:", decryption(encryption(plain_text, key), key))
    elif choose.upper() == 'D':
        cipher_text = input("Enter cipher text: ")
        print("Decryption result:", decryption(cipher_text, key))
    else:
        print("Enter correctly!")
        getChoose()  
      
#encryption process 
def encryption(plain_text, key):
    key = key.upper()
    plain_text = plain_text.upper()
    encrypted_plain_text = ""
    j = list(key)
    k = 0 #to keep index of key letters
#    s3 = ""
    for i in plain_text :
        if i.isalpha(): 
#            s1 = ord(i) + ord(j[k])
#            s2 = (s1 - 2 * ord('A')) % 26
#            s3 += chr(s2 + ord('A'))         
# simplified as one line   
            encrypted_plain_text += chr((ord(i) + ord(j[k]) - 2 * ord('A')) % 26 + ord('A'))
        else :
            k -= 1 
        k = k + 1
        k = k % len(key)
    return encrypted_plain_text  

#decryption process 
def decryption(cipher_text, key):
    key = key.upper()
    decrypted_cipher_text = ""
    j = list(key)
    k = 0 
#    s3 = ""
    for i in cipher_text :
        if i.isalpha():
#            s1 = ord(i) - ord(j[k])
#            s2 = (s1 + 26) % 26
#            s3 += chr(s2 + ord('A'))
# simplified as one line
            decrypted_cipher_text += chr((ord(i) - ord(j[k]) + 26) % 26 + ord('A'))
        else:
            #if text character is not a letter 
            #then index of key doesn't need to be incremented
            k -= 1 

        k = (k+1) % len(key)
    return decrypted_cipher_text        

if __name__ == '__main__':
    getChoose()
