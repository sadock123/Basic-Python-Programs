n=str(input())
sum=0
max_sum=0
for i in range(len(n)-1):
    if (n[i]==n[i+1]):
        sum=sum+1
    else: 
        sum=0
    max_sum=max(max_sum,sum+1)
if max_sum>=7:
    print("YES")
else:
    print("NO")