li=[[1,2],[3,4],[5,6]]
li_1=[[3,4],[5,7],[1,2]]

# result=[]
# for i in li:
#     if i not in li_1:
#         result.append(i)
# for i in li_1:
#     if i not in li: 
#         result.append(i)
# print(result)

# second method
res=[]
for i in li:
    res.append(i)
for i in li_1:
    if i not in li:
        res.append(i)
print(res)
