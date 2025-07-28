#4.Sum of Digits (5 marks)Take an integer input from the user and calculate the sum of its digits. (e.g., input 123 → output 6)

number=int(input("Enter a number: "))
sum=0
if number>=0 :
    while number>0 :
        num=number%10
        sum=sum+num
        number=number//10
    print(sum)
else :
    print("its a negative number")    