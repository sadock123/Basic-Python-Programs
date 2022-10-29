n=int(input())
list1=list(map(int,input().split()))
k=0.0
for i in range(n):
    k=k+float(list1[i]/n)
print(k)