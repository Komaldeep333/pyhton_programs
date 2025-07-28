# dict {}: collection of key value pairs
# heterogeneous,mutable,ordered, allow duplication[value not keys].
a={"name":"Komal","Rollno":2233634,"course":"Btech","stream":"CSE"}
# print(a)
# print(type(a))
# print(len(a))
# print(a["name"])          #keys can be of both integer and string datatype


# d={"movies":["Avengers,Kalki,Sitare Zameen par"],
#    "hero":["Kartik","Amir","Abhishek"],
#    "herione" :["tapsee","deepika"],
#    "year" :[2012,1013]
# }
# print(d["movies"])


#Functions of dictionaries
# print(d.get("movies"))
#d.update({"year":2012})     #Year will only contain 
# print(d)
#d.pop("year")
#print(d)             year key will be removed

# print(d.keys())
# print(d.values())
# print(d.items())


#overwritten or updation
# d["movies"]="Bhool Bhuliya 3"
# print(d)
d={"movies":["Avengers,Kalki,Sitare Zameen par"],
   "hero":["Kartik","Amir","Abhishek"],
   "herione" :["tapsee","deepika"],
   "year" :[2012,2013],
   400:"Success"
}
d["year"][0]=2019
d[400] = "False"
print(d)



#Traversing

# for i in d:
#     print(i,d[i])

# for i in d.keys():
#     print(i)    
# for i in d.values():
#     print(i)
# for i,j in d.items():
#     print(i,j)
# for i in a:
#    if type(a[i])==int: 
#         #type of values or here we dont has any int so other will be printed because we all have is list
#          print(i,a[i])
#    else:
#         print("other")        


# user defined dictionary



# dict={}
# n=int(input("Enter the limit: "))
# for i in range(n):
#    k=input("Enter the keys: ")
#    v=input("Enter the values: ")
#    dict[k]=v
# print(dict)     






























