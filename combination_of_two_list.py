import itertools
from itertools import permutations
li=[1,2,3]
l1=['a','b']
empty_list=[]
temp=itertools.permutations(li,len(l1))
for ele in (temp):
    a=zip(ele,l1)
    empty_list.append(list(a))
    print(empty_list)
