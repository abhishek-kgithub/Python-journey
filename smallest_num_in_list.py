# li=[9,8,7,6,5,4,3,2,1]
# li.sort()
# print("smallest number :", li[0])


li=[]
num=int(input("enter the length of list :"))
for i in range(1,num+1):
    ele=int(input(f'enter the element {i}: '))
    li.append(ele)
print("the smallest element is :",min(li))