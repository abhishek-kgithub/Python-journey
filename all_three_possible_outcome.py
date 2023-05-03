def comb(li):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(li[i],li[j],li[k])

li=[5,6,7]
comb(li)