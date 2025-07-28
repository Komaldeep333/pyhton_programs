#1.
# number=int(input("Enter a number: "))
# if number>0 and number%2==0 :
#     print("number is positive and even")
# elif number>0 :
#     print("Positive odd")
# elif number<0 :
#     print("number is negative")  
# else :
#     print("number is zero")          


#3. Factorial
# fact=1
# a=int(input("Enter a number: "))
# for i in range(1,a+1,1) :
#     fact=fact*i
# print(fact)

#5. 
# for i in range(51) :
#     print(i,end=" ")
#     if i%3==0 :
#         print("Fizz")
#     elif i%5==0 :
#         print("Buzz")
#     elif i%3==0 and i%5==0 :
#         print("FizzBuzz")
#     else :
#         print("the number is not divisble by 3 and 5")

#10.

# string=input("Enter a string: ")
# a=0
# b=0
# c=0
# for i in string:
#     if i.isdigit() :
#         a=a+1
# print(a)
# for i in string:
#     if i.isalpha() :
#         b=b+1
# print(b)
# for i in string:    
#     c=c+1  
# print(c)


#7.
# a=int("Enter a number: ")
# b=int("Enter a number: ")
# opt=input("Enter any operator (+, -, *, /, %, **): ")
# if opt=="+" :
#     print(a+b)
# elif opt=="-" :
#     print(a-b)
# elif opt=="*" :
#     print(a*b)
# elif opt=="/" :
#     if  b==0 :
#         print("zero is entered")
#     else :
#         print(a%b)
    
    
# elif opt=="%" :
#     if  b==0 :
#         print("zero is entered")
#     else :
#         print(a%b)
# elif opt=="**" :
#     print(a**b)
# else :
#     print("no operator is choosen")


#4. Addition

# number=int("Enter a integer: ")
# t=0
# while number>0 :
#     s=number%10
#     t=t+s
#     number=number/10
# print(t)

#2.Prime

# number=int(input("Enter the number: "))
# if number>1 :
#     for i in range(2,number) :
#         if(number%i==0) :
#             print("number is not prime")
#         else :
#             print("number is prime")    

# else :
#     print("number is not prime")


#.


# number=int(input("Enter a number for loop: "))
# for i in range(number) :
#     for j in range(i+1):
#         print(" ",end="")
        
# print() 
a=0
# print(a,type(a))

# b=str(a)
# print(b,type(b))

print(str(a),type(str(a)))
print(float(a),type(float(a)))
print(bool(a),type(bool(a)))
