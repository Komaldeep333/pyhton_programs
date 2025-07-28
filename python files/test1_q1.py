# 1. Number Classification (5 marks)Write a Python program that takes a number from the user and prints:

# "Positive Even" if the number is positive and even

# "Positive Odd" if the number is positive and odd

# "Negative" if the number is negative

# "Zero" if the number is zero

number=int(input("Enter a number: "))
if number>0 :
    if number%2==0 :
        print("Positive Even")
    else :
        print("Positive Odd")  
elif number<0 :
    print("Negative Number")
else :
    print("Zero")    

        