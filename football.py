from collections import Counter
n=int(input())

arr=[]
for i in range(n):
    k=str(input())
    arr.append(k)
l=Counter(arr)
k1=1

m=max(l, key=l.get)
print(m)
