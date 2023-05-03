def sortedarry(li):
    for i in range(len(li[0])):
        sortedcolumn = sorted(li,key=lambda x:x[i])
        print("sorted araay specific to column {}.\{}".format(i,sortedcolumn))

if __name__ == '__main__':

   li=[['c',2000],['java',1988],['python',1900],['rust',1899]]
   sortedarry(li)
