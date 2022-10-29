n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
flag=0
for i in (l1):
    if i==n:
        flag=1
for j in (l2):
    if j==n:
        flag=1
if (flag==1):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")