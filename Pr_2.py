
                 #  Dictionary
# a. Write a Python script to check whether a given key already exists in a dictionary.

di={1:10,2:20,3:30,4:40,5:50} #creating dictionary
def is_key(x): # function to check key is present or not
  if x in di:
    print("Key is present")
  else:
    print("Key is not present")
    
is_key(5)   #calling function
is_key(9)

#b. Write a Python script to merge two Python dictionaries.

dic1={1:10, 2:20}

dic2={3:30, 4:40}

d=dic1.copy();

d.update(dic2);

print(d)

# c. Write a Python program to sum all the items in a dictionary.

d={1:10,2:20,3:30,4:40,5:50}

print(sum(d.values()));
print(sum(d.keys ()));

#d. Write a Python script to add a key to a dictionary.

d={0: 10, 1: 20}

d.update({2:30})
print(d)
#Write a Python script to concatenate following dictionaries to create a new one.

d1={1:10, 2:20}

d2={3:30, 4:40}

d3={5:50,6:60}

d=d1.copy()
d.update(d2)
d.update(d3)
print(d)
