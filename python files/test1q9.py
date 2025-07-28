#9. Type Conversion Validator (5 marks)Take input from the user and attempt to convert it into int, float, and bool.
#  Print each result and handle any conversion errors using try-except blocks.


n = input("Enter any value: ")

try:
     # integer conversion
    i = int(n)
     # float conversion
    f = float(n)
     #  boolean conversion
    c=int(n)
    d=bool(c)
    
except Exception as e:
    print("Conversion failed at step:", e)
else:               # Code that runs if NO exception was raised in try block
    print("As int:   ", i, type(i))
    print("As float: ", f, type(f))
    print("As bool:  ", d, type(d))         







