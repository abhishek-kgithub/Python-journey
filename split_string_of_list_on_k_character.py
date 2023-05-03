li=["I am abhishek","hello","world"]
k= " "
res=[]
for i in li:
    j=i.split(k)
    res.extend(j)
print(res)

res=k.join(li).split(k)
print(res)