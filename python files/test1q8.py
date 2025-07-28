#8. Star Pyramid Pattern (5 marks)Write a Python program to print the following pattern (for n = 5):

#     *
#    ***
#   *****
#  *******
# *********

for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()                

#Lets break down to understand
#i=0
# for j in range(0, 5):  # spaces
#     print(" ", end="")   # prints 5 spaces
# for j in range(0):       # no stars  - range(0) means:"Start at 0, stop before 0"So... it doesn’t even start! The loop runs 0 times, which means:👉 The code inside the loop is skipped.
#     print("*", end="")   # prints nothing
# for j in range(1):       # 0 + 1 = 1 star
#     print("*", end="")   # prints 1 star

#output
#     *
#--------------------------------------------------------------------------------------------------------
#i=1
# for j in range(1, 5):   # prints 4 spaces
# for j in range(1):      # prints 1 star
# for j in range(2):      # prints 2 stars

#output
#    ***
#--------------------------------------------------------------------------------------------------------------

#i=2
# for j in range(2, 5):   # prints 3 spaces
# for j in range(2):      # prints 2 stars
# for j in range(3):      # prints 3 stars


#output
#   *****

#--------------------------------------------------------------------------------------------------------------
#i=3
# for j in range(3, 5):   # prints 2 spaces
# for j in range(3):      # prints 3 stars
# for j in range(4):      # prints 4 stars
#output
#  *******

#--------------------------------------------------------------------------------------------------------------
#i=4
# for j in range(4, 5):   # prints 1 space
# for j in range(4):      # prints 4 stars
# for j in range(5):      # prints 5 stars
#output
# *********

#final output
#      *
#     ***
#    *****
#   *******
#  *********




