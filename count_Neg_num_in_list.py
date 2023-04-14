li=[1,2,-1,-5,-6,-6,-6,-6,-5,8,9]
positive_count=0
negative_count=0
for i in li:
    if i>=0:
        positive_count+=1
    else:
        negative_count+=1

print(positive_count)
print(negative_count)
