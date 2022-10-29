test=int(input())
while(test>0):
    m=int(input())
    k=list(map(int,input().split()))
    l=max(k)
    print(k.index(l)+1)

    test=test-1