
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

                         # SET
#a. Write a Python program to add member(s) in a set and clear a set

s={1,"a",2,3}
s.add(5)
print(s)

s.update(["b","c"])
print(s)


#b. Write a Python program to remove an item from a set if it is present in the set.

s={1,2,3,"a","b"}

s.remove(2)
print(s)

#c. Write a Python program to create an intersection, Union, difference of sets.

s1={1,2,3,4,"abc","d","e"}
s2={2,3,6,5,"abc","e"}

print(s1|s2)  #Union
print(s1&s2)  #intersection
print(s1-s2)  #difference

#d. Write a Python program to find maximum and the minimum value in a set.

s={1,2,3,4,5}

print(max(s))
print(min(s))

#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

s=[1,2,2,2,3,5,5,7,7,7,7]
temp=0
count=0
index=0
for i in range(0,len(s)):
    temp=s.count(s[i])
    
    if(temp>count):
        count=temp;
        index=i;
        
common=s[index]
print("Common element is ", common) # for list
print("No of counts is ",count)

# for tuple
t=(1,2,3,4,5,5)
li=list(t)  
temp=0
count=0
index=0
for i in range(0,len(li)):
    temp=li.count(li[i])
    
    if(temp>count):
        count=temp;
        index=i;
        
common=li[index]
print("Common element is ", common) # for list
print("No of counts is ",count)

# for dictionary

di={1:10,2:20,3:30,3:30}

d=list(di.keys())
temp=0
count=0
index=0
for i in range(0,len(d)):
    temp=d.count(d[i])
    
    if(temp>count):
        count=temp;
        index=i;
        
common=d[index]
print("Common element is ", common) # for list
print("No of counts is ",count)


                                         # Tuple
#a. Write a Python program to create a tuple with different data types.

t=(1,"RAJ",12.2)

print(t)

# b. Write a Python program to create a tuple with numbers and print one item.

t=(1,2,3,4,5)

print(t[0:1])

#c. Write a Python program to add an item in a tuple.

t1=(1,2,3,4,5)

t2=(6,7,8,9)

t2=t1+t2;

print(t2)

#d. Write a Python program to convert a tuple to a string.

t=("R","A","J")
st=''.join(t)
print(st)

t1=("My","Self")

st=' '.join(t1);
print(st);

#e. Write a Python program to find the length of a tuple.

t=(1,2,3,4,5,6,7)

l=len(t)

print(l)



     
  
                   