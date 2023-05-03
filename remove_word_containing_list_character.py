li=["geeks","is","for","best","geeks"]
k=["g","o"]
res=[]
flag=False
for ele in li:
    for i in k:
        if i not in ele:
            flag=False
        else:
            flag=True
            break
    if(flag==False):
        res.append(ele)
print(res)

# using filter and lambda function

res=list(filter(lambda x:not any(y in x for y in k),li))
print(res)