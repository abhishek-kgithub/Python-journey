li=[44,55,68,689,21,79,8,64]
# li.sort()
# print(li[-2]) 

# second method

new_li=set(li)
print(new_li)
new_li.remove(max(new_li))
print(max(new_li))