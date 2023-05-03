li=[1,2,2,5,8,4,4,8]
l1=[]
count=0
print(li)
for item in li:
	if item not in l1:
		count += 1
		l1.append(item)
print(l1)
print(count)

