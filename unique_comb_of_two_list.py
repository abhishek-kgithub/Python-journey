li=[1,2,3]
l1=['a','b']

unique_comb=[]
for i in range(len(li)):
    for j in range(len(l1)):
        unique_comb.append((li[i],l1[j]))
print(unique_comb)