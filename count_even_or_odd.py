# li=[int(x) for x in input().split()]
li=[1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
for num in li:
    if num % 2 ==0:
     even_count+=1
    else:
     odd_count+=1
    
print("even count :",even_count)
print("odd count :",odd_count)

