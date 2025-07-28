# # Q1. Create a list of 10 number and print the list
#<---------------------------------------Answer----------------------------------------------->


# a=[]
# n=int(input("Enter the limit for list: "))
# for i in range(n) :
#     v=int(input("Enter the values: "))#  for all valus   or int(input("Enter the values: ")) for integer values only
#     a.append(v)
# print(a) 



# # Q2. Create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list
#<--------------------------------Answer------------------------------------------------>


# a=[1,10,100,3,6,8]
# #print(a)
# a.insert(3,59)
# #print(a)
# a.append(5)
# print(a)
# print(len(a))


# # Q3. create a list of 10 elements and print all elements are even locations
# # Example:
# #     x = [1,4,2,42,4,6,2,56,4,56]
# #     Result is: 1 2 4 6 56 56
#<------------------------------------Answer------------------------------------------------->


# x=[1,4,2,42,4,6,2,56,4,56]
# print("Result is:", end=' ')
# for i in range(0,len(x),2) :
#     print(x[i],end=" ") 


# # Q4. create a list with values ["Gaurav",12,23,33.33,"Sharma",True] and print only elements which are string
#<------------------------------------------Answer------------------------------------------


# a=["Gaurav",12,23,33.33,"Sharma",True] 
# for i in a:
#     if type(i)==str :
#         print(i)


# # Q5. add all the number present in above list
#<-------------Answer--------------------------------------------------------------->


# a=["Gaurav",12,23,33.33,"Sharma",True] 
# s=0
# for i in a:
#     if type(i)==int or type(i)==float :
#         s=s+i
# print(s)


# # Q6. Create a list with 5 friends and ask user a friend name and add that name in the friend list, 
# and print the list after that ask user to most important friend and add that friend at user choice
# # Ex: [1,2,3,4,5]
# # -> Enter anothe fiend: Raju
# # [1,2,3,4,5,"Raju"]
# # --> Most import afiedn: Billa
# # --> Please location for billa: 1
# # [1,"Billa",3,4,5,"Raju"]

#<---------------------------------------------Answer---------------------------------------------------



a=["Komaldeep","Komalpreet","Muskan","Mayank","Mohit"]
print(a)
f=input("Enter another friend name: ")
a.append(f)
print(a)
i=input("Most important friend: ")
l=int(input(f"Choose location from (0 to {len(a)}) for {i}? "))
a.insert(l,i)
print(a)

  

