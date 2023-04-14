def copying(li):
    new_li=li[:]
    return new_li
li=[1,2,3,4,5]
li2=copying(li)
print(li2)
# print(type(li2))