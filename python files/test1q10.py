#10. Count Digits, Alphabets, and Specials (5 marks)Write a program that takes a string input 
# from the user and counts how many digits, alphabets, and special characters it contains.
d=0
a=0
c=0
string=input("Enter any string:")
for i in string:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        a=a+1
    else:
        c=c+1
print("Digits are:",d)
print("Alphabets are:",a)
print("Special Characters are:",c)        





