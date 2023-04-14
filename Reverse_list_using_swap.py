def reverse(li):
    left=0
    right=len(li)-1
    while(left<right):
        li[left],li[right]=li[right],li[left]
        left+=1
        right-=1
    return li
li=[1,2,3,4,5]
print(reverse(li))