#Reversse a given string without using reverse built in functions
string = input("Enter a string: ")

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string 

print("Reversed string:", reversed_string)

#check if a string is palindrome
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string 
if string == reversed_string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#count no of vowels and consonants in string
string=input("enter anything")   
vowels_count=0
consonants_count=0
vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1

print("vowels count:",vowels_count)      
print("consonants count:",consonants_count)    

#remove spaces from a string
string = input("Enter a string: ")
string1 = string.replace(" ", "")
print("String without spaces:", string1)


#count frequency of character in string

a=input("enter anything :")
b={}
for x in a:
    if x not in b:
        b[x]=1
    else:
        b[x]+=1
print(b)            





