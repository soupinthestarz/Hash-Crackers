# Author: Ava Chong
# Created in November 2024

#hash cracking to allow for faster 'GUESS ATTACK' on proavided hashes
import hashlib
hash1 = "482c811da5d5b4bc6d497ffa98491e38"
hash2 = "9af870b687c9c080740c108296069cae"
hash3 = "979d5b78613520f02d4118968683fbbb"
hash4 = "a44b6b00e5eebd7494e1fd00658685e2"
hash5 = "7b0f81bdd2b24ba32cb27f6c16e6b900"

hashes = [hash1, hash2, hash3, hash4, hash5]
found = 0
while found == 0:

    guess = input("What is your guess: ")

    #hash user's guess
    guessHash = hashlib.md5(guess.encode())
    guessHexDigest = guessHash.hexdigest()
    for x in hashes:
        #cycle through all given hashes and compare to user's hash
        #compare hex digest to hash in cycle
        if guessHexDigest == x:
            print(guess, "is the correct password for", x)
            found = 1 #if a password is found, found is set to true
    #if not found, tell user
    if found == 0:
        print(guess, "is not the password to any given hash!")