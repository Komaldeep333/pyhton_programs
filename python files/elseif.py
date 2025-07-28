print("Enter your choice of hotel")
print("1.Taj")
print("2.grund")
print("3.makan")
hotel=input("Select the one: ")
if hotel =="Taj" :
    print("Select the meal I will show you price")
    print("1.Burger")
    print("2.Pizza")
    print("3.cookies")
    
    item=input("Select the item: ")
    if item=="Burger":
        print("Price is 100")
    elif item=="Pizza" :
        print("Price is 200")
    else :
        print("price is 50")
                
elif hotel =="grund" :
    print("Select the meal I will show you price")
    print("1.Burger")
    print("2.Pizza")
    print("3.cookies")
    
    item=input("Select the item: ")
    if item=="Burger":
        print("Price is 1000")
    elif item=="Pizza" :
        print("Price is 2000")
    else :
        print("price is 5000")
   
    print("You Selected grund")
elif hotel =="makan" :
    print("You Selected makan")
else :
    print("You Selected nothing")            