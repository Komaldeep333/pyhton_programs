#Tuple:  heterogeneous ,ordered,allows duplication,indexed,immutable or tuple is collection of items    ,()
#a=("hello",223,"world",3.5,True,"abc",1.1)
# print(a)
# print(type(a))
# print(len(a))
# print(a[3])
# print(a[-2])
# print(a[0])
# print(a[0][4])
#a.append(24)      #error because of tuple is immutable

#Slicing

# print(a[1:5])
# print(a[::])
# print(a[2:7])
# print(a[2:10:2])
# print(a[6:1:2])
# print(a[6:1:-2])
# print(a[::3])
# print(a[::-1])

# b=("abc",55,8,[True,5.6,("hello",5,0.4),55],False,0)
# print(b[2])
# print(b[3][3])
# print(b[3][2][2])
# print(b[3][2][0][1])
# print(b[3][2][1])


#Functions
c=("hello",223,"world",3.5,True,"abc",1.1)
# print(c.count(3.5))
# print(c.index("abc"))

# for i in c:
#     print(i)
# for i in c:
#     if type(i)==str:
#         print(i)
#     else:
#         print("other data type")  

x=0
for i in c:
    if type(i)==int or type(i)==float:
        x=x+i
print(x)                      