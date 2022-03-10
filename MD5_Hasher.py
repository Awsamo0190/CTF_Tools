#!/bin/python

import hashlib #imports hash library

word = input("Whats the word: ") #asking for what to hash
hash = hashlib.md5(word.encode()) #encoding the text 
md5_hash = hash.hexdigest() #this the variable for the hash created
print(md5_hash) #this prints the hash

#This is a simple script the takes input and converts it to a MD5 Hash
