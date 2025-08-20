#prime  number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")
    
#output    
#Enter a number: 7
#7 is a prime number.


#Factorial
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
#output    
#Enter a number: 6
#The factorial of 6 is 720
#fibonacci upto n terms
n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
        
#output
#Enter the number of terms: 8
#0 1 1 2 3 5 8 13 



#sum of digits
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10         

print("Sum of digits:", sum)   

#output
#Enter a number: 587
#Sum of digits: 20

#reverse number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10       
    rev = rev * 10 + digit 
    num //=10            

print("Reversed number:", rev)
#output
#Enter a number: 678
#Reversed number: 876





    
