test=int(input())
while (test>0):
    count=0
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    for i in range(n-1):
        for j in range(n):
            if l1[j] in l2:
                l1[j]=0
                continue
            elif l1[i]>= l1[j] and l1[i]!=0: 
                l2.append(l1[i])
                l1[i]=0
                count=count+1
            
            
    test=test-1
    print(count)