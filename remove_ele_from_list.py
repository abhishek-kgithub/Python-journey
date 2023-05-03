# li=[1,1,1,1,5,6,98,7,4,1,1,1]
# ele=1
# x=[]
# for i in li:
#     if i!=ele:
#      x.append(i)
# print(x)

# second method

def remove_ele(li,ele):
   res=[i for i in li if i!=ele]
   return res
   
li=[1,1,1,1,5,6,98,7,4,1,1,1]
b=remove_ele(li,1)
print(b)


