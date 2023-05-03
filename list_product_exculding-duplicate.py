# li=[1,3,5,6,3,5,6,1]
# product=1
# l1=[]

# for i in li:
#     if i not in l1:
#         l1.append(i)
# for ele in l1:
#     product=product*ele
# print(product)

# second method

def prod(li):
    res=1
    for ele in li:
        res=res*ele
    return res

li=[1,3,5,6,3,5,6,1]
res=[]
[res.append(x) for x in li if x not in res]
res=prod(res)
print(res)
