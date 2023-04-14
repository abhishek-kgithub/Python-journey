a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
li=[]
for i in range(a,b+1):
    if i%2!=0:
        li.append(i)
print(li)
