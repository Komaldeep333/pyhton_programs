#----------------sum function
# def sum(x,y):
#     c=x+y
#     print("Sum is: ",c)

# a=int(input("Enter first number: "))   
# b=int(input("Entetr second number")) 
# sum(a,b)
# # sum()     error
# # sum(a)    error
# # sum(b)
# sum(4,5)   # run and use 4,5 instead of a,b

#--------------even/odd
# def evenodd(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")    

# a=int(input("Enter number: "))
# evenodd(a)  

#-----------local or global variable
# # local and global var

# a=10   # a is a global var
# def fun():
#     b=7  #b is local var
#     print(a+b)
# fun()
# print(a)
# print(b) #error
# pi=22/7
# def cal():
#     r=int(input("Enter radius: "))
#     res=pi*(r*r)
#     print("Area of circle is:",res)
#     print(r)
# cal()  
# print(pi)
#print(r)  #error because of local variable

# Arbitrary arguments(passing 0 or more arguments to function)

# def abc(*n):
#     print(n)
# abc()
# abc(2)
# abc(2,4,5)        #shows result in form of tuple
# abc(4,5,6.7,"jkj")    
    

# def gh(a,*b):
#     print(a,b)

# gh()   #error  required one element as 'a'
# gh(3)    #no error 


#Key Arbitrary(**)
# def f(**a):
#     print(a)

# f()      #run
# f(x=3,y=7.1,name="komal",a=True)    #shows result in form  of key value pair
# #f(b,**a)    same as above like in arbitrary

# def home(a,b,**c):
#     print(a,b,c)

# home(a=2,b=3,x=3,y=7.1,name="komal",h=True)    #variables used in function and function calling should be same

# Lambda function
# x = lambda n: print(n)
# x(4)
# y=lambda a,b: print(a+b)
# y(3,4)
# z=lambda e: print("even") if e%2==0 else print("odd")
# z(4)
# k=lambda *a: print(a)
# k(2,3,4,5) 
# l=[2,3,4,5]
# r=map(lambda n: n*n,l)
# print(list(r))

# u=lambda **n: print(n)
# u(t="home",h="book")
# map function----------------------------------------------------------------------
# l=[2,3,4,5]
# def square(n):
#     return n**2
# a=list(map(square,l))
# print(a)
#                    OR

# l=[2,3,4,5]
# r=map(lambda n: n*n,l)        just repalced lambda with square function
# print(list(r))

    
# def fg(n):
#     return n**2           # only works on iteratable just to manipulate the data
# m=map(fg,2)               # gives errors
# print(m)

#Filter----------------------------------------------------------------------------------
# just used for filter out the content only according to user choice


# l=[2,3,4,5]
# r=filter(lambda n: n%2==0,l)        
# print(list(r))
# x="komaldeep kaur"
# f=filter(lambda i:i=="e",x)
# a=list(f)
# print(len(a))








 

