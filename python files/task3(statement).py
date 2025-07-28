# Question 1. Printing the month
# number=int(input("Enter number of your choice(1-12) "))
# if number==1 :
#     print("January")
# elif number==2 :
#     print("February")
# elif number==3 :
#     print("March")
# elif number==4 :
#     print("April")
# elif number==5 :
#     print("May")
# elif number==6 :
#     print("June")
# elif number==7 :
#     print("July")
# elif number==8 :
#     print("August")
# elif number==9 :
#     print("September")
# elif number==10 :
#     print("October")
# elif number==11 :
#     print("November")
# elif number==12 :
#     print("December")
# else :
#     print("You are entering the wrong month number")  





# Question 2. 
# first=int(input("Enter first number "))
# second=int(input("Enter second number "))
#-----------------------------------------------------------------------------------------------------------------------
# if first==second :
#     print("Both numbers are equal")
# else :
#     print("Numbers are not equal")
#  #-----------------------------------------------------------------------------------------------------------------------   
# if first>second :
#     print("First number is bigger")
# else :
#     print("Second number is bigger")  
# #------------------------------------------------------------------------------------------------------------------------
# if first<=second :
#     print("First is smaller or equal to second")
# else :
#     print("First number is greater")
#------------------------------------------------------------------------------------------------------------------------
# if first>second :
#     print(("Komal\n")*5)
   
   
     
# else :
#     print(("Kaur")*3)
    




# Question 3.
# string1=input("Enter first string :")
# string2=input("Enter first string :")
# if string1==string2 :
#     print("Both strings are equal")
# else :
#     print("Strings are not equal")
# #=================================================OR============================================================
# print(string1 is string2)  #False because ids are different







# Question 4.  
# s1=input("Enter first string :")
# s2=input("Enter first string :")
# n1=int(s1)#================================this can only be done if you enter "10" as string not "abc" as string
# n2=int(s2)
# print(n1 is n2)




# Question 5.
budget=int(input("Enter your travel budget (in USD):"))#============like 2500
if budget>=4000 :
    
    print("1. Europe")
    print("2. America")
    print("3. Canada")
    country = int(input("\nSelect a country by entering the corresponding number: "))
    if country == 1:
        print("You selected: Europe")
        print("We suggest you visit these places in Europe:")
        print("1. Russia")
        print("2. Spain")
        print("3. Germany")
        
    elif country == 2:
        print("You selected: America")
        print("We suggest you visit these places in America:")
        print("1. Mexico")
        print("2. Cuba")
        
    elif country == 3:
        print("You selected: Canada")
        print("We suggest you visit these places in Canada:")
        print("1. Toronto")
        print("2. Vancouver")
    else:
        print("Invalid selection.")

elif 2000 <= budget < 4000:
    print("1. Germany")
    print("2. Australia")
    print("3. Malaysia")
    country2 = int(input("\nSelect a country by entering the corresponding number: "))

    if country2 == 1:
        print("\nYou selected: Germany")
        print("We suggest you visit these places in Germany:")
        print("1. Berlin\n2. Munich\n3. Hamburg")
    elif country2 == 2:
        print("\nYou selected: Australia")
        print("We suggest you visit these places in Australia:")
        print("1. Sydney\n2. Great Barrier Reef\n3. Melbourne")
    elif country2 == 3:
        print("\nYou selected: Malaysia")
        print("We suggest you visit these places in Malaysia:")
        print("1. Kuala Lumpur\n2. Langkawi\n3. Penang")
    else:
        print("Invalid choice.")
elif 1000 <= budget < 2000:
    print("1. Thailand")
    print("2. Vietnam")
    print("3. Nepal")
    country3 = int(input("\nSelect a country by entering the corresponding number: "))

    if country3 == 1:
        print("\nYou selected: Thailand")
        print("We suggest you visit these places in Thailand:")
        print("1. Bangkok\n2. Phuket\n3. Chiang Mai")
    elif country3 == 2:
        print("\nYou selected: Vietnam")
        print("We suggest you visit these places in Vietnam:")
        print("1. Hanoi\n2. Halong Bay\n3. Ho Chi Minh City")
    elif country3== 3:
        print("\nYou selected: Nepal")
        print("We suggest you visit these places in Nepal:")
        print("1. Kathmandu\n2. Pokhara\n3. Chitwan")
    else:
        print("Invalid choice.")

else:
    print("Sorry, your budget is too low")        


     

