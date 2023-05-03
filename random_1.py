li=['gfgBest','forGeeks','andComputerScience']
res=[]
for ele in li:
    temp=[[]]
    for i in ele:
        if i.isupper():
        #  print(i)
           temp.append([])
        #  print(temp)
        temp[-1].append(i)
    # print(temp)
    res.append(' '.join(''.join(ele) for ele in temp))
print(res)
