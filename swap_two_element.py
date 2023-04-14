def swapElement(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list


list=[1,2,3,45,4]
pos1,pos2=1,3
print(swapElement(list,pos1-1,pos2-1))