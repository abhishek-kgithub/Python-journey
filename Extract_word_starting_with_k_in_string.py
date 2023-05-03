li=['abhishek','adarsh','patil','adamya']
k='a'
res=[]
for i in li:
    # temp=i.split()
    for j in i.split():
        if j[0]==k:
            res.append(i)
            
print(res)
