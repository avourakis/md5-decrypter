import hashlib
import os

def hash(word):
    # Hash a word
    no_whitespace = string.replace("\n", "")
    return hashlib.md5(no_whitespace).hexdigest()

def decrypt(md5_hash, dict_path):
    # Decrypt md5
    with open(dict_path, "r") as dict_file:
        for word in dict_file:
            enc_word = hash(word)
            if(enc_word == md5_hash):
                return word

def md5_decrypter():
    
    while True:
        # Get path of dictionary
        dict_path = input("Drag dictionary file: ")

        # Get hash from user
        md5_hash = input("Enter Hash: ")

        # Check inputs
        if(dict_path == "" and md5_hash == ""): 
            print("Error: Empty dictinary file. Please put one file")
            print("Error: Empty hash.")
            md5_decryptor()
        elif(dict_path == ""):
            print("Error: Empty dictinary file.")
            dict_file = input("Drag dictionary file: ")
        elif(md5_hash == ""):
            print("Error: Empty hash.")
            md5_hash = input("Enter Hash: ")
        else:
            break

    # Decrypt hash
    result = decrypt(md5_hash, dict_file)
    print("Cracked hash: ", result)    

if __name__ == "__main__":
    md5_decrypter()

