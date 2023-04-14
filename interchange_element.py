def swapList(list):
    # get=list[-1],list[0]
    list[0],list[-1]=list[-1],list[0]
    return list

newList=[1,2,3,4,5]
print(swapList(newList))