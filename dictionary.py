# Author: Ava Chong
# Created in November 2024

#basic hash cracking to allow for a "DICTIONARY ATTACK" on proavided hashes based on given dictionary of words.
import hashlib
hash1 = "36e5371ad91c9d2d09e9d7c0e76055db" #first hash
hash2 = "a44b6b00e5eebd7494e1fd00658685e2" #first hash


words = ["cyberspace", "cybercrime", "cybersecurity", "authentication", "authorization", "firewall", "hacktavist", "ransonware", "spoofing", "NIST"] #dictionary list
#cycle through each provided word 
for x in words:
    str1 = x
    #hash eaech provided word and get string
    hashObj = hashlib.md5(str1.encode())
    hexDigest = hashObj.hexdigest()
    #compare hex digest
    if hexDigest == hash1:
        print("password for", hash1, "is:", str1)
    if hexDigest == hash2:
        print("password for", hash2, "is:", str1)