def evenList(li,n=0):
    if n==len(li):
        exit()
    if li[n] %2 == 0:
        print(li[n],end=" ")
    evenList(li,n+1)


li1=[5,2,3,4,5,6,7,8,9,5,6,9,8]
print(evenList(li1))