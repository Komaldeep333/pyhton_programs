#1.

# c=0
# string=input("Enter a string: ")
# for i in string :
#     if i=='i'  or i=='o' or i=='e' or i=='a' or i=='u' or i=='A' or i=='E' or i=='U' or i=='I' or i=='O':
#         c=c+1
# print(c)

#2.
# string=input("Enter a String: ").lower()
# a=b=c=d=e=0
# a=string.count('o')
# b=string.count('e')
# c=string.count('i')
# d=string.count('a')
# e=string.count('u')
# print("o- ",a)
# print("e- ",b)
# print("i- ",c)
# print("a- ",d)
# print("u- ",e)

#3.

# str="aioueAIUOE"
# c=0
# a=i=e=o=u=0
# string=input("Enter a string: ")
# for chh in string :
#      if chh in  str :  
#         c=c+1
# print("Total vowels: ",c)
# for ch in string :
#     if ch=='a' or ch=='A' :
#         a=a+1
#     elif ch=='i'or ch=='I' :
#         i=i+1
#     elif ch=='e' or ch=='E':
#         e=e+1
#     elif ch=='o'or ch=='O' :
#         o=o+1
#     elif ch=='u' or ch=='U' :
#         u=u+1
    
# print("a- ",a)
# print("i- ",i)
# print("o- ",o)
# print("e- ",e)
# print("u- ",u) 


#4.


# s=input("Enter a String: ").lower()
# a=0
# for i in range(len(s)) :
#     if s[i]=='a' :
#         a=a+1
#         if a==2 :
#             print("2nd 'a' found at index:", i)
#             break   
    
# if a<2 :
#     print("character 'a' doesnot occur more than once")        
        
#5.
# c=0
# l=-1
# s=input("Enter a String:").strip()
# for i in range(len(s)) :
#     if s[i]=='i' :         #strip function removes the extra space from right and left side of the wholw string
#         c=c+1
#         if c==5 :
#             l=i
#             break
# print("Last i location is ",l)

#6.

# s=0
# a=0
# string=input("Enter a string:")
# print("Total characters in string: ",len(string))       #Total characters in string
# print("Total  number of 'a' in string: ",string.count('a'))  #Total a character in string
# for i in string :
#     if i.isdigit() :
#         s=s+int(i)  
# #print(s)            #Sum of digits 
# for i in string :
#     if not i.isspace() :
#         a=a+1
# print("Sum of digits in string: ", s)
# print("Total characters in string excluding space: ",a)    

#7.

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# if a>b and a>c :
#     print(a," is greater")
# elif b>c and b>a :
#     print(b," is greater")
# else :
#     print(c," is greater")         

#8. 

# number=int(input("Enter a number: "))
# if number%3==0 :
#     if number%5==0 :
#         if number%10==0 :
#             print("The ",number," is divisible by 3 and 5 and 10")
#         else :
#             print("The number is not divisible by 10 but by 3 and 5") 
#     else :
#         print("The number is not divisible by 5 and 10")        
    
# else :
#     print("The number is not divisible by 3,5,10")
    




