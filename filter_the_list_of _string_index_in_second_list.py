li=['abhishek','maurya','and','rahul','has','friend']
l1=['is ok ','hi ok','jd','not ok','jj','hello ok']

res=[]
k='ok'
for ele1,ele2 in zip(li,l1):
    # print(ele1,ele2)
    if k in ele2:
        res.append(ele1)
print(res)

# list comprehension 
res=[ele1 for ele1,ele2 in zip(li,l1) if k in ele2]
print(res)
