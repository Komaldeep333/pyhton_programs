# set : heterogeneous,unordered,unindexed,dont allow duplication,mutable
# a={"hello",223,"world",3.5,True,"hello",1,223}
# print(a)
# print(type(a))
# print(len(a))


#Functions
# a.add("abc")
# a.remove("hello")
# a.discard(223)
# a.pop()
#a.clear()

s1={1,2,3}
s2={4,5,6,7}
s3={1,2,3,4,5,6,7}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.issubset(s3))
print(s3.issuperset(s1))
print(s3.issubset(s1))
print(s1.issuperset(s3))

