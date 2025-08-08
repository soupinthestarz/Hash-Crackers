# Author: Ava Chong
# Created in November 2024

import hashlib
from itertools import product #itertools to replace loops for salt crack
hash1 = "f241b830d1944e06d9786f18ed4a431f"
hash2 = "918317f46fd5fed8e46c876c7c957a04"
hash3 = "517372dae26e82b7867a4513cad6e50e"
hash4 = "557884242e3eec9563556678e912307f"
hash5 = "bc85ae1dd7e5e9916e87cf71416399ce"

bruteFHash = "49f68a5c8493ec2c0bf489821c21fc3b"
# Bruteforce algo
# imbedded for loop: check a - z
    # check a-z
    # hash and compare
    #if match, return true, cout the combination that matches.
# if no match from previous algorithm, then run a third imbedded loop and compare

#basic bruteforce for a 2 character, lowercase password
letters = "abcdefghijklmnopqrstuvwxyz"


for combo in product (letters, repeat=2):
    # store guess
    guess = "".join(combo)

    # convert guess to hex hash with md5 algo
    hashObj = hashlib.md5(guess.encode())
    hexDigest = hashObj.hexdigest()
    # compare digest to burte force hash and return password if found.
    if hexDigest == bruteFHash:
        print("The password for brute force algo is:", guess)
        break  # stop search after password is found
       


# SALTED CRACK --> crack a password with given cracked password and a possible 5 character salt on the beginning of the password consisting of lower case letters and numbers.

chars = "abcdefghijklmnopqrstuvwxyz1234567890" # set of characters salt could be derived from.
passwords = ["password123", "unr", "covid", "NIST", "nancy"] # given passwords
foundPasswords = {} # to store cracked passwords
# Dictionary of hashes for quick lookup
hashes = {
    "hash1": hash1,
    "hash2": hash2,
    "hash3": hash3,
    "hash4": hash4,
    "hash5": hash5
}

# Reverse lookup: hash -> name
# value --> md5 hash string
# key --> name of hash

hashLookup = {value: key for key, value in hashes.items()}
# product gives all possible combinations of input items, allowing for repetition --> CARTESIAN PRODUCT, as repetitions are allowed, so it is not permuatations instead.
for combo in product(chars, repeat=5):
    prefix = "".join(combo)
    for suffix in passwords:
        # add salt to front of password
        guess = prefix + suffix
        # get hex hash from string
        hashObj = hashlib.md5(guess.encode())
        hexDigest = hashObj.hexdigest()
        #compare hash against hash in dictionary
        if hexDigest in hashLookup and hashLookup[hexDigest] not in foundPasswords:
            foundPasswords[hashLookup[hexDigest]] = guess
            print("Password for", hashLookup[hexDigest], "is", guess)

            if len(foundPasswords) == len(hashes):
                print("5/5 Passwords found, terminating search") # stop search after all passwords have been found
                exit()

