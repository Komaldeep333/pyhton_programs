#1 Write a function to convert temperatures from Celsius to Fahrenheit.
#Formula	
#(0°C × 9/5) + 32 = 32°F  where c is 0 degree
#<-----------------------------------------------Answer-------------------------------------------------->
# def temp(c):
#     f=(c*(9/5))+32
#     print("Temperature in Fahrenheit is: ",f)


# x=int(input("Enter the temperature in Celsius(degrees): "))    
# temp(x)

#2 Implement a function to find the greatest common divisor (GCD) of two numbers.

#<-----------------------------------------------Answer-------------------------------------------------->
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#     #or
# # def gcd(a, b):
# #     while b:
# #         a,b = b,a%b
# #     return a


# x=int(input("Enter the first number: "))      #36
# y=int(input("Enter the second number: "))     #60
# result=gcd(x,y)
# print("The gcd of ",x,"and",y,"is ",result)
# Explanation


# gcd(36, 60)          # a = 36, b = 60 → call gcd(60, 36 % 60 = 36)
# gcd(60, 36)          # a = 60, b = 36 → call gcd(36, 60 % 36 = 24)
# gcd(36, 24)          # a = 36, b = 24 → call gcd(24, 36 % 24 = 12)
# gcd(24, 12)          # a = 24, b = 12 → call gcd(12, 24 % 12 = 0)
# gcd(12, 0)           # b = 0 → return a = 12  (GCD is found)



#3 Develop a function to merge two lists into a single sorted list.
#<-----------------------------------------------Answer-------------------------------------------------->
# def merge(list1, list2):
#     a = list1 + list2   # '+' operator is used to combine the 2 lists
#     a.sort()         # Sort the list 
#     return a         # Now return the sorted list


# l1=[3,5,6,7,2]
# l2=[6,4,5,2,9]

# r=merge(l1,l2)
# print("Merge and sorted list of ",l1," and",l2,"is ",r)

#4 Write a function to count the number of vowels in a given string.
#<-----------------------------------------------Answer-------------------------------------------------->

# def  str_count(str):
#     c=0
#     for i in string :
#         if i=='i'  or i=='o' or i=='e' or i=='a' or i=='u' or i=='A' or i=='E' or i=='U' or i=='I' or i=='O':
#             c=c+1
#     print("Total number of vowels in ",str,"is ",c)

# string=input("Enter a string: ")
# str_count(string)

#5 Create a function to find the second largest number in a list.
#<-----------------------------------------------Answer-------------------------------------------------->

# def number(list):
#     list.sort()
#     print(list)
#     c=0
#     for i in range(len(list)):
#         c+=1
#         if c==len(list)-1:
#             print(list[i])
#             break
# l=[3,6,5,8,9,4]
# number(l)

#6.Implement a function to remove duplicate elements from a list.
#<-----------------------------------------------Answer-------------------------------------------------->
# def duplicate(l1):
#     print("Original list is: ",l1)
#     a=list(set(l1))
#     return a
    
# l=[3,4,5,3,4,6,7,3,2,7,6,4]
# r=duplicate(l)
# print("After removal of duplicates: ",r)


#7 Develop a function to calculate the sum of all prime numbers up to a given number.

# def number(n):
#     total = 0
#     for i in range(2, n + 1):  # Start from 2
#         for j in range(2, i + 1):
#             if i % j == 0:
#                 break
#         if i == j:
#             total += j
#     return total

# var=int(input("Enter the number: "))
# print(number(var))  

#8.Write a function to check if a given year is a leap year.

# def leapyear(year):

#     if (year%4==0 and year%100!=0) or year%400==0:                         
#         print("Its a leap year")
#     else: 
#         print("Its not a leap year")    
# y=int(input("Enter a year to check leap or not:"))  
# leapyear(y)  


#9 Create a function to reverse the words in a given sentence.

# def reverse_string(s):
#     for i in range(0,len(s)):
#         print(s[i],end="")
#     print()        
#     for j in range(len(s),0,-1):
#         print(s[j-1],end="")


# string=input("Enter a string: ")
# reverse_string(string)












