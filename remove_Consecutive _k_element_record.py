# li=[(4,5,6,3),(5,6,6,9),(1,3,5,6),(6,6,7,8),(4,3,6,6)]
# K=int(input("enter the k element :"))
# result=[]
# for item in li:
#     skip=False
#     for i in range(len(item)-1):
#         if item[i]==K and item[i+1]==K:
#             skip=True
#             break
#     if not skip:
#         result.append(item)
# print(result)

# second method
def consecutive_k(li,K):
    result=[]
    for item in li:
        skip=False
        for ele in range(len(item)-1):
            if item[ele]==K and item[ele+1]==K:
             skip=True 
             break
        if not skip:
            result.append(item)
    return result

li=[(4,5,6,3),(5,6,6,9),(1,3,5,6),(6,6,7,8),(4,3,6,6)]
a=consecutive_k(li,6)
print(a)