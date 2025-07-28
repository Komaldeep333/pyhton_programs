#3. Factorial Calculator (5 marks)Write a Python program that takes an integer input 
# and prints its factorial. Implement using a loop.
number=int(input("Enter a number to find its factorial: "))
f=1
if number>0 :
    for i in range(1,number+1) :
        f=f*i
    print("The factorial of ",number," is ",f)    
else :
    print("Its a negative number")