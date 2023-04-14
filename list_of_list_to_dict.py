li=[['a','b',1,2],['c','d',3,4],['e','f',4,5]]
result=dict()
for ele in li:
    result[tuple(ele[:2])]= tuple(ele[2:])
print(str(result))


# second method

res={tuple(i[:2]):tuple(i[2:]) for i in li}
print(res)