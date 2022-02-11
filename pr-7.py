# ID:-20CE105
#Name:- Patel Sumankumar
                       # Practical-7
# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. 
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, 
# since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
# Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. 
# Your task is simple. Given a string, you need to tell if it is a lapindrome. 
# Input: 
# 6 
# gaga 
# abcde 
# rotor 
# xyzxy 
# abbaab 
# ababc 
# Output: 
# YES 
# NO 
# YES 
# YES 
# NO 
# NO


import collections;
testCases = int(input())  # number of test cases
while testCases:        # iterate over the number of test cases
    testCases -= 1
    string = input()        # get the string
    halve = len(string) // 2    # get the half length of the string
    if len(string) % 2 == 0:      # if the length of the string is even
        if sorted(string[:halve]) == sorted(string[halve:]):  # if the first half is equal to the second half
            print('YES')
        else:                                # if the first half is not equal to the second half
            print('NO')
    else:                            # if the length of the string is odd
        if sorted(string[:halve]) == sorted(string[halve + 1:]):   # if the first half is equal to the second half
            print('YES')
        else:
            print('NO')