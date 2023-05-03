li=[(4,3,5,4,4),(3,4,5),(4,4,4),(5,6,4,4,4)]
K=4
N=3
# res=[]
# for ele in li:
#     if ele.count(K)==N:
#         res.append(ele)
# print(res)

# Second method
res=list(filter(lambda x : x.count(K)==N,li))
print(res) 