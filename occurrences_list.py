# def occurance(li,x):
#    a= li.count(x)
#    return a

# li=[1,2,3,4,5,5,5,5,1,5,6,6,4,4,4]
# b=occurance(li,1)
# print(b)


def occurance(li,x):
    count=0
    for ele in li:
        if (ele==x):
            count+=1   
    return count
li=[1,1,1,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5]
x=int(input("Enter occurance number: "))
b=occurance(li,x)
print('{} as occur {} times'.format(x,b))