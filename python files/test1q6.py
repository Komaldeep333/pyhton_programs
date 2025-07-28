#6.List Input and Stats (5 marks)Take 7 numbers from the user (using a loop), store them in a list, 
# then print the minimum, maximum, and average of those numbers.
x=0
a=[]
print("Enter the seven numbers")
for i in range(7):
    n=int(input("Enter number: "))
    a.append(n)
a.sort()
print(a)
print("Maximum number is: ",a[6])
print("Minimum number is: ",a[0])
for i in a:
    x=x+i
y=x/len(a)
print("Average of numbers: ",y)


