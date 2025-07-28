#1.
number=int(input("Enter the number: "))
for i in range(number) :
    print("Komaldeep")


#2.
n=int(input("Enter a number: "))
for i in range(3,33) :
    print(n,"*",i,"=",n*i)



#3.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a<b :
    for i in range(a,b) :
        print(i,end=" ")
elif a>b:
    for j in range(a,b,-1) :
        print(j,end=" ")
else :
    print("same numbers")        

#4.
name=input("Enter your name: ")
age=int(input("Enter the current age: "))
current_year=int(input("Enter current year: "))
expected_year=int(input("Enter the expected year: "))            #information upto next 20 years
for i in range(expected_year) :
    print("hey",name,"in",current_year+i,"you are",age+i,"year old")

 
               