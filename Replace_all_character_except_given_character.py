li=["a","g","j","a","j","a"]
k="a"
res=[]
for i in li:
    if i==k:
        res.append(i)
    else:
        res.append("*")
print(res)

# using comprehension

res=[i if i==k else "*" for i in li]
print(res)