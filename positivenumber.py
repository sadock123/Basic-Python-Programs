n=int(input())
while n>0:
    n=n-1
    count=0
    l=int(input())
    list1 = []
    list1= list(map(int,input().split()))
    for i in range(0,l):
        for j in range(i,l):
            if (list1[i]*list1[j] >= 0):
                count = count+1
    print(count)