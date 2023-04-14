a=int(input("enter the first number :"))
b=int(input("enter the second number :")) 
li=[]
for i in range(a,b+1):
    if i%2==0:
        # print(i,end=" ")
        li.append(i)
print(li)

