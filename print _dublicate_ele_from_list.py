li=[1,2,3,1,2,3,1,2,3,5,6,9,6,5,4,5,6,3,2,1,4]
i=0
l1=[]
for i in li:
    n=li.count(i)
    if n>1:
        if l1.count(i)==0:
            l1.append(i)
print(l1)