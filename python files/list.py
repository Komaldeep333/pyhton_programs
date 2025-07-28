#List is collection of items in a particular order
#properties: mutable,allow duplicacy,orderd,indexed,heterogeneous,[](representation)
# a=[4,"hello",5.6,66,"abc",True]
# print(a)
# print(type(a))
# print(len(a))
# print(a[2])
# print(a[-3])
# print(a[4][1])
#print(a[5][2]) Error


#Slicing
# print(a[::])
# print(a[2:5])
# print(a[0:7:2])
# print(a[0:4:3])
# print(a[2::4])
# print(a[5:1:])
# print(a[::-2])   #Reverse the start and end points

# important
# l=[77,True,[3.4,22,"bye",[6,"hello",3],55,4],True]
# print(l[1])
# print(l[3])
# print(l[2][1])
# print(l[2][3][2])
# print(l[2][3][1])
# print(l[2][3][1][4])


#Functions in lists
# li=[4,"hello",5.6,66,"abc",True]
# li.append(86)        #value
# print(li)
# li.insert(2,"bye")     #index and value
# print(li)
# li.remove(4)        #value
# print(li)
# li.pop(2)          #index
# print(li)
# #li.clear()
# print(li.count("hello"))      #value
# li.reverse()
# print(li)
# li.index("hello")         #value


# lii=[3,5,1,6,8,3]
# lii.sort()        #ascending order
# print(lii)
# lii.sort(reverse=True)      #descending order
# print(lii)



a=[4,"hello",5.6,66,"abc",True]
# for i in a:
#     print(i)
# for i in range(len(a)) :      #if we used len fxn then it prints index values when we used i but if we use list directly then it
#     print(i,a[i])                         #uses index values  here i is index and a[i] is value but in above i is value

# for i in a :
#     if type(i)==int :
#         print(i)
# x=0
# for i in a :
#     if type(i)==int or type(i)==float :
#         x=x+i
# print(x)         

# x=0
# a=["123","abc",55,"hello",True,"22",34,False] 
# for i in a:
#     if type(i)==int or type(i)==str :
#         if type(i)==int or i.isdigit() :
#             x=x+int(i)
# print(x)



# x=0
# a=["123","abc",55,"hello","22",34] 
# for i in a:
#     if type(i)==str :
#         if i.isdigit() :
#             x=x+int(i)
# print(x)        


# x=0
# a=["123","abc","hello","22"] 
# for i in a:
    
#     if i.isdigit() :
#         x=x+int(i)            #isdigit is only valid on strings
# print(x)        


#Make a list with value given by user
# a=[]
# n=int(input("Enter the limit for list: "))
# for i in range(n) :
#     v=input("Enter the values: ")#  for all valus   or int(input("Enter the values: ")) for integer values only
#     a.append(v)
# print(a)  


# a=[]
# n=int(input("Enter the limit for list: "))
# for i in range(n) :
#     v=input("Enter the values: ")
#     if v.isdigit() :
#         a.append(int(v))
#     elif v=="True" or v=="False" :
#         a.append(bool(v))
#     else :
#         a.append(v)  
# print(a)              

# a=[]
# print("Enter end to stop the list")
# while True :
    
#     v=input("Enter the values: ")
#     if v.isdigit() :
#         a.append(int(v))
#     elif v=="True" or v=="False" :
#         a.append(bool(v))
#     elif v=="end":
#         break

#     else :
#         a.append(v)  
# print(a)       

#Zip function in lists
# a=[2,3,4,5]
# b=[6,7,8,9]
# c=zip(a,b)    #prints the object only
# # print(c)
# d=list(c)
# print(d)
# for i in d :
#     print(i)
# for i,j in d:
#     print(i,j)   
    

#list comprehension 

# l=[i for i in range(1,10)]        
# print(l)  
l=[i for i in range(1,20) if i%2==0]
print(l)
#                 Or
l = []                         # Start with an empty list
for i in range(1, 20):         # Loop from i = 1 to 19
    if i % 2 == 0:             # Check if i is even
        l.append(i)            # If it is, add it to the list


li=["even" if i%2==0 else "odd" for i in range(1,20)] 
print(li) 
lii=[[i,j] for i in range(5) for j in range(3)]
print(lii)

# When you're filtering values (include only some):
# if goes after the for

# → ✅ [i for i in range(1, 20) if i % 2 == 0]

# When you're choosing what value to add (like "even" or "odd"):
# if goes inside the expression

# → ✅ ["even" if i % 2 == 0 else "odd" for i in range(1, 20)]

# what to print is always at first