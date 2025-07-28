#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

#Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


list1=["Black", "Red", "Maroon", "Yellow"]
list2=["#000000", "#FF0000", "#800000", "#FFFF00"]
c=zip(list1,list2)
print(c)
# d=list(c)

r=[]
# for i,j in d:
for i,j in c:          #Traversing from tuple  made in zip
    di={}
    di['color_name']=i
    di['color_code']=j
    r.append(di)
print(r)    
   


