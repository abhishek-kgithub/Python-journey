li=["abhishek","patil"]
k=10
i=0
for ele in li:
    if i+len(ele)>k:
        print(k-i)
        break
    else:
        i+=len(ele)
else:
    print("k is beyond the list")

# second method
# res=[i[0] for ele in enumerate(li) for i in enumerate(ele[1])]
# res=res[k]
# print(res)
