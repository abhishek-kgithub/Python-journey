li=['gfg','is','best']
l1=[0,1,0,1,0,0,0,1,2,0]
# res=[li[idx] for idx in l1]
# res=list(map(lambda ele:li[ele], l1))
# print(res)
res=[]
for i in l1:
    res.append(li[i])
print(res)
    

