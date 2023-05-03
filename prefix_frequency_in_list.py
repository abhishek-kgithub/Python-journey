li=['abhi','abhishek','abhinav','patil']
count=0
k='abh'
for i in li:
    if i.startswith(k):
        count=count+1
print(count)

# second method
res=sum(i.startswith(k) for i in li)
print(res)