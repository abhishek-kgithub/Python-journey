li=[4,5,6,7,8,9]
res=False
i,j=3,10
for ele in li:
    if i<ele<j:
        res=True
        break
print(res)