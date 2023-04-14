import numpy as np
li=[0,-2,6,-8,-5,6,-2,-1,-6,-7]
neg_num=list(filter(lambda x: (x<0),li))
print(neg_num) 

# second method
temp=np.array(li)
neg_num1=temp[temp<0]
print(neg_num1) #in this output comma will disappear