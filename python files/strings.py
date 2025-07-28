
#Indexing
a="hello world"
#print(a)
#print(type(a))
#print(len(a))
# print(a[8])
# print(a[-1])
# print(a[4])
#print(a[3.4])        #error

#Slicing
#b="Drag me to hell"
# print(b)
# print(type(b))
# print(len(b))
# print(b[::])
# print(b[2:7])
# print(b[:9:1])
# print(b[5:13:2])
# print(b[::2])
# print(b[14:3:1])
# print(b[::-1])

#Functions-: we can access any function of string with "."
# a="my name is anTHony134 gonzaliz"
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.count("a"))
# print(a.count("a",0,10))
# print(a.find("a"))          #index and find are same
# print(a.rfind("a"))
# print(a.index("a"))
# print(a.startswith("m"))      #returns true of false
# print(a.endswith("z"))

# functions related to string characters
#a="hello 123"
# print(a.isalnum())
# print(a.isdigit())
# print(a.isalpha())
# print(a.islower())
# print(a.isupper())
# print(a.isspace())
# print(a.istitle())

#splitt
# a="how are you today"
# print(a.split())
# print(a.split("o"))

#Strings with loops and elseif condition

a="how are you"
# for i in  a:
#     print(i,end="")       #Stringa are direct traversed,i viists every character in string
# for i in range(len(a)) :  # directly prints the string without traversing
#     print(a[i])    
# for i in a:
#     if i=="o" :
#         print(i)
# s=0
# x=input("Enter a string: ")
# for i in x:
#     # if i.isupper() :
#     #if i.isupper() or i.isdigit() :
#     if i.isdigit() :
#         s=s+int(i)
# print(s)

s=input("Enter a String: ")
for i in range(len(s)) :
    if s[i]=='o':
        print(s[i],i)       # correct explanation to use index and index values in case of strings but if we are using without 
                             #length function then we can use index function(inbuilt)

