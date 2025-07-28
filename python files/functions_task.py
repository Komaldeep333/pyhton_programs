#1.Write a program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number, 
# and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
#<-----------------------------Answer--------------------------------------------------------------->

# def num():
#     # FizzBuzz program: prints numbers from 1 to 50 with specific substitutions

#     for i in range(1, 51):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# num()                    


#2.Write a program to print all prime numbers between 1 and 100
# m=int(input("Enter first number:"))
# n=int(input("Enter first number:"))

#<-----------------------------Answer--------------------------------------------------------------->
# def number():
#     for i in range(2,100):              #it is between 1 and 100 so starts with 2 
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if i==j:
#             print(j)  
# number()         


# 3.Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F    
#<-----------------------------Answer--------------------------------------------------------------->
# def grade(x):
#     if x>90 and x<100:
#         print("Grade is: A")
#     elif x>80 and x<89:
#         print("Grade is: B")
#     elif x>70 and x<79:
#         print("Grade is: C")
#     if x>60 and x<69:
#         print("Grade is: D")
#     else:
#         print("Grade is: F")


# n=int(input("Give any score between 0 to 100:"))
# grade(n)



 #4.Write a program that prints the multiplication table (from 1 to 10) for a given number

#<-----------------------------Answer--------------------------------------------------------------->
# def table(n):
#     for i in range(1,11):
#         print(n,"x",i,"=",n*i)

     
# x=int(input("Enter the number to have the multiplication table:"))
# table(x)



#5.Write a program to create a list of the squares of the even numbers from 1 to 20.

  #<-----------------------------Answer---------------------------------------------------------------> 

def square(n):
    return n**2
l=[]
for i in range(1,21):
   if i%2==0:
      l.append(i)

a=list(map(square,l))
print(a)
           