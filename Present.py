n=int(input())
x=list(map(int,input().split()))
l=[]
for i in range(1,n+1):
    l.append(x.index(i)+1)

print (*l)