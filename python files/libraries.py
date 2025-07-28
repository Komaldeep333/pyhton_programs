import random as rd
# a=rd.randint(1,20)
# print(a)

# b=rd.randrange(0,20,3)
# print(b)


# c=rd.random()   #between 0 and 1
# print(c)

# d=rd.choice(["pen","pencil","copy","eraser"])
# print(d)
print()
print("                                 Welcome to the Rock-Paper-Scissor Game!!                            ")
print()
a=0       # for user
b=0       #for machine


for i in range(5):
    u=input("Its your turn! Please choose(rock,paper,scissor):")
    m=rd.choice(["rock","paper","scissor"])
    print("Machine chooses: ",m)
    print("User chooses: ",u)
    if u==m:
        print("draw")
    elif u=="rock" and m=="paper":
        print("machine wins")
        b+=1
    elif u=="paper" and m=="scissor":
        print("machine wins")
        b+=1
    elif u=="rock" and m=="paper":
        print("machine wins")
        b+=1
        
    elif u=="scissor" and m=="rock":
        print("machine wins")
        b+=1
        
    elif u=="paper" and m=="rock":
        print("you wins")
        a+=1
        
    elif u=="scissor" and m=="paper":
        print("you wins")
        a+=1
        
    elif u=="rock" and m=="scissor":
        print("you wins")
        a+=1
        
    else:
        print("you have choosen wrong")    
print("Machine wins ",b," times")
print("User wins ",a," times")

                
        









#Math Library
# import math
# a=math.pi
# print(a)
# print(math.cbrt(8))
# print(math.ceil(3.45))
# b=math.sin(90)
# print(b)
# c=math.cos(90)
# print(c)
# d=math.sin(0)
# print(d)



#Datetime Library
# import datetime as dt
# a=dt.datetime.now()
# print(a)
# b=dt.date.isoformat(a)   
# print(b)
# print(dt.datetime.time(a))
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)
# print(a.date())
# print(a.day)
# print(a.month)
# print(a.year)













   


