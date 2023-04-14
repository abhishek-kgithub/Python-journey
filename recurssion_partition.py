def count_part(n,m):
    if n==0:
        return 1
    elif m==0 or n<0:
        return 0
    else:
        return count_part(n-m,m)+count_part(n,m-1)
    
print(count_part(9,5))