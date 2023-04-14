li=[0,-2,6,-8,-5,6,-2,-1,-6,-7]
i=0
l1=[]
for i in li:
    if i>=0:
        l1.append(i)
print(l1)

# second method

positive_num=list(filter(lambda x : (x>=0),li))
print(positive_num)
a=l1.count(6)
print(a)