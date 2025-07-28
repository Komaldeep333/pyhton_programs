
#Operators

# Arthmetic Operators  
# + - * / // % **

# a=17
# b=5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) floor division as 17/5 is 3.5 but returns 3
# print(a%b)
# print(a**b)


#Assignment Operators
# = += -= *= /= //= %= **=

# a=10
# print(a)

# a+=5   # a=a+5
# print(a)

# a-=3
# a*=4
# a/=5
# a%=7

# print(a)


#Comparison/Relational Operators
# == != > < >= <=

# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)


#Logical Operators
# and, or, not

# a=10
# b=20
# c=30

# print(a<b and b>c)
# print(a<b or b>c)
# print(not(a<b and b>c))


#Membership Operators
# in, not in

# a="hello world"
# print("hel" in a)
# print("hel w" in a)

# print("hel" not in a)
# print("hel w" not in a)


#Identity Operators
# is, is not

# a="hello"   ////shows same memory address for both a and b because we declared them same when input variable is not used
# b="hello"
a=input("enter a value ")      
b=input("enter b value ")

#print(id(a),id(b))
print(a is b)
#print(a is not b)