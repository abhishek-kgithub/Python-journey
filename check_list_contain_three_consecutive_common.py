li=[4,4,4,5,8,22,22,22,4,8,8,8,2]
res=[]
size=len(li)
for i in range(size-2):
    if li[i]==li[i+1] and li[i+1]==li[i+2]:
        res.append(li[i])
print(res)