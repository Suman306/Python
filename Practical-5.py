def swap_case(s):  #creating function swap_case to swap the characters in the string
    
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower()); #if the character is uppercase, it will be converted to lowercase
        elif(char.islower()==True):
            Output += (char.upper()); #if the character is lowercase, it will be converted to uppercase
        else:
            Output += char; #if the character is not a letter, it will be kept as it is
    return Output;
   

if __name__ == '__main__':
    print("Enter a string: ");
    s = input()      #taking input from the user
    result = swap_case(s)
    print(result)    #printing the result