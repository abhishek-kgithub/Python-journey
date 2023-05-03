li=["abhishek","is","goodboy","abhishek","like","Gaming"]
k="abhishek"
res=[]
for i in li:
    if i.startswith(k):
       res.append([i])
    else:
       res[-1].append(i)
print(res)
