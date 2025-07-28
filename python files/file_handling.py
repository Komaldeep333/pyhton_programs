
#Writing or creating a filr ist tym
# f=open('hello.txt','w')
# f.write("Hello i am doing training")
# f.close()

#Reading 
# f=open('hello.txt','r')
# print(f.read())

#Appending

# f=open('hello.txt','a')
# f.write("\nI think i am doing nice in this")
# f.close()

# f=open('hello.txt','r')
# print(f.read())


# import time

# f=open('hello.txt','r')
# for i in f:
#     time.sleep(1)
#     print(i)

#Exception Handling

# try:
#     statements           if try got any exception it will run but it goes to finally always if an eror comes yet
                            #but after errors no statement will run in try.so write the leftover code in except or finally
# except exception as e:
#     statements
# finally:
#     statement    

# try:
#     a=10
#     b=0
#     l=[2,3,4,5]
#     print(a/b)
#     print(l[8])
# except Exception as e:
#     print(e) 
# finally:
#     print("HELLO")
           

try:
    a=10
    b=0
    l=[2,3,4,5]
    print(a/b)
    print(l[8])
except ZeroDivisionError as e:
    print("exception",e) 
except IndexError as e:
    print(e)     
finally:
    print("HELLO")
           






    