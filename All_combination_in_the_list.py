def combination(li,r):
    a =tuple(li)
    n=len(a)
    if r>n:
        return
    l1=list(range(r))
    yield tuple(a[i] for i in l1)
    while True:
        for i in reversed(range(r)):
            if l1[i] !=i+n-r:
                break
        else:
            return
        l1[i]+=1
        for j in range(i+1,r):
            l1[j]= l1[j-1]+1
        yield tuple(a[i] for i in l1)

x=[2,3,1,6,4,7]
for i in combination(x,2):
    print(i)