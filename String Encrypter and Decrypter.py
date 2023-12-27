'''
Programmer: Raj Shah
Version: 1.0
Description: for ENCRYPTION: take characters in a string and shift each character by a random number from 1-26, meaning y becomes d when the shift is 5. For DECRYPTION: takes the characters and applies the shift backwards with given integers.
Date: July 25, 2022

Algorithm:
import random module

create function encrypt with parameter msg
    define rand_nums
    create loop in range of the length of msg
        create the random numbers

    create loop in range of the length of msg
        check if msg at i is a letter
        
            define index as the index of each character

            check if index + the random number is greater than 26
                if so, add index and random number and subtract 26

                otherwise,
                    add index and random number

                change msg at i to be the character of the index we just found
    
    return the msg and random numbers

create function decrypt with parameter msg and l
    create loop in range of length of msg
        check if msg at i is a letter

            define index as the index of each character

            if index minus the character is less than or equal to 0
                subtract 26 - l[i] - index

            otherwise,
                subtract the character from the index

            change msg at i to be the character of the index we just found

    return the msg

create infinite loop
    get input from user for message to encrypt
    call the encrypt function

    get input from user for message to decrypt
    get list input from user for positive integers
    call the decrypt function
            

pre-condition: a string to encrypt, a string to decrypt, and a list of positive integers between 1-26 inclusively
post-condition: a tuple output with string and list for encryption, and a string output for decryption
'''
import random

def encrypt(msg):
    rand_nums = []
    for i in range(len(msg)):
        rand_nums.append(random.randint(1, 26))    # create list of random numbers

    for i in range(len(msg)):
        if msg[i].isalpha() == True:
            index = ord(msg[i]) - ord("a") + 1    # using ascii functions, get the index of the character. i.e., 'b'=2, 'e'=5, 'z'=26, etc.
            
            if index + rand_nums[i] > 26:
                index = (index + rand_nums[i]) - 26   # check if the index is over 26 (last index in alphabet)
            else:
                index = index + rand_nums[i]

            msg[i] = chr(index + ord("a") - 1)   # change the character within the list using the index

    return "".join(msg), rand_nums

def decrypt(msg, l):
    for i in range(len(msg)):
        if msg[i].isalpha() == True:
            index = ord(msg[i]) - ord("a") + 1
            
            if index - l[i] <= 0:
                index = 26 - (l[i] - index)     # check if the index is less than or equal to 0 (last index in alphabet)
            else:
                index = index - l[i]     # subtract the given number from the character index

            msg[i] = chr(index + ord("a") - 1)

    return "".join(msg)

while True:
    encrypt_msg = list(input("Enter a string to ENCRYPT: ").lower())   # get user input, convert it to lowercase, then call functions
    print(encrypt(encrypt_msg))

    decrypt_msg = list(input("Enter a string to DECRYPT: ").lower())
    prompt = "Enter a list of " + str(len(decrypt_msg)) + " positve integers: "
    l = eval(input(prompt))
    print(decrypt(decrypt_msg, l))

