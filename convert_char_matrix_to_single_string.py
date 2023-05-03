li=[['a','b','h'],['i','s','h'],['e','k']]
res= ["".join(i for ele in li for i in ele)]
print(res)
res=[]
for ele in li:
    for i in ele:
        # "".join(i)
        # res.append(i)
     print("".join(i),end="")
