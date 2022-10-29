
test=int(input())


while (test>0):
    count=0
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    for i in range(k):
        if l1[i]> k:
            count=count+1
        
   
    print(count)
    
    test=test-1   
    