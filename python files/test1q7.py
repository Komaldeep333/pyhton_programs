#7. Advanced Calculator (5 marks)Create a calculator that takes two numbers and an operator (+, -, *, /, %, **) 
# as input and prints the result. Also handle division/modulo by zero.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
opt=input("Enter any operator (+, -, *, /, %, **): ")
if opt=="+" :
    print(a+b)
elif opt=="-" :
    print(a-b)
elif opt=="*" :
    print(a*b)
elif opt=="/" :
    if  b==0 :
        print("Error divison by zero")
    else :
        print(float(a/b))
    
    
elif opt=="%" :
    if  b==0 :
        print("Error divison by zero")
    else :
        print(a%b)
elif opt=="**" :
    print(a**b)
else :
    print("no operator is choosen")
