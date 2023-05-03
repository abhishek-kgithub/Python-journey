li=["gfg"," ","    ","abhishek"]
res=[]
for ele in li:
    if ele.strip():
        res.append(ele)
print(res)

# using list comprehension
res=[ele for ele in li if ele.strip()]
print(res)