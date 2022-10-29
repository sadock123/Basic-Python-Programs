n=int(input())
k=[]
for i in range(n):
    x=list(map(int,input().split()))
    k.append(x)
sum1=0
sum2=0
sum3=0
for j in range(len(k)):
    m=0
    sum1=sum1+ k[j][m]

for j in range(len(k)):
    m=1   
    sum2=sum2+k[j][m]
for j in range(len(k)):
    m=2
    sum3=sum3+k[j][m]
if sum1==0  and sum2==0 and sum3==0:
    print("YES")
else:
    print("NO")
    