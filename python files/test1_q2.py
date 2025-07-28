#2. Prime Number Checker (5 marks)Write a Python program to check whether a given number is prime or not. 
# Use a loop and conditional logic.

number=int(input("Enter a number: "))
c=0
if number>0 :
    for i in range(1,number+1) :
        if number%i==0 :
            c=c+1                                                   #Zero is whole number,so its not prime number
    if c==2 :
        print("Its a prime number")
    else :
        print("Its not a prime number")

else :
    print("Its a negative number")

             