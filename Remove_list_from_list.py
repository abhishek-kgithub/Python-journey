
# res=list(filter(None,li))
# print(res)

# second method

def empty_list(xyz,value=True):
    print(value)
    a=[]
    for ele in xyz:
        if ele:
            a.append(ele) 
    return a

    
li=[4,5,[],8,99,[],[]]
b=empty_list(li,False)
# print(empty_list(li))
print(b)