# ID:-20CE105
#Name:- Patel Sumankumar
                       # Practical-6
# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
# Sample Input 
# 4 
# bcdef 
# abcdefg 
# bcde 
# bcdef 
# Sample Output 
# 3 
# 2 1 1 


import collections;

N = int(input())  # number of words
d = collections.OrderedDict() # ordered dictionary
for i in range(N):  # iterate over the number of words
    word = input()  # get the word
    if word in d:    # if the word is already in the dictionary
        d[word] +=1   # increment the count
    else:
        d[word] = 1  # else add the word to the dictionary
print(len(d));         # print the length of the dictionary
for k,v in d.items():
    print(v,end = " ");   # print the count of the word