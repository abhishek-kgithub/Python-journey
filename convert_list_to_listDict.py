li=["aryan",3,"is",8,"my",2,"good",5,"friend",1]
key_list=["name","number"]
n=len(li)
result=[]
for ele in range(0,n,2):
    result.append({key_list[0]:li[ele], key_list[1]:li[ele+1]})

print(result)

    