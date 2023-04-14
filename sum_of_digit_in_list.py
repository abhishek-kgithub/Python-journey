li=[12,13,14,56,81]
print("The original list :" , li)
result=[]
for ele in li:
    sum=0
    for digit in str(ele):
        sum=sum+int(digit)
    result.append(sum)
print("the list after alter :" ,result)