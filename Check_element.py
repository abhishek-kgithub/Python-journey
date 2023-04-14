# li=[1,2,3,6,5,4,7,8,9]
# a=int(input("enter the element that given in list :"))
# result=any(a in li for a in li)
# print(str(bool(result)))

li=[1,2,3,54,15,56,98]
b=int(input("enter the element that given in list :"))
a=li.count(b)
if a>0:
    print("The number is exixt")
else:
    print("the number is not exixt")