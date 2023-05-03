# li=[45,5,23,10,9]
# a=len(li) -1
# res=[]
# for i in range(1,a):
#     r=max(li[i+1],li[i-1])
#     res.append(r)
# print(res)

# second method

li=[1,4,34,420,54,66,7,8,9]
b=len(li)-1
res=[]
for i in range(1,b):
    if li[i+1]>=li[i-1]:
        res.append(li[i+1])
    else:
        res.append(li[i-1])
print(res)