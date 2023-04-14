li=[1,2,5,9,8,15,45]

x=list(map(str,li))
y="-".join(x)
b=input("Enter the element that you arte lokking for:")
if y.find(b) != -1:
    print("element is present in list")
else:
    print("Element is not present in list")