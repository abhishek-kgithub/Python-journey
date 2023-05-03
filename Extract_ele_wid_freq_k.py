li=[4,6,4,3,3,3,4,3,7,8,8]
k=2
res=[]
for i in li:
    freq=li.count(i)
    if freq>k and i not in res:
        res.append(i)
print(res)