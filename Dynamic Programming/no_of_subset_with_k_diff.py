def dp(arr,sum1):
    n,m= len(arr)+1,sum1+1
    arr2=[[0]*m]*n
    for i in range(n):
        for j in range(m):
            if j==0:
                arr2[i][j]=1
    for i in range(n):
        for j in range(m):
            if (arr[i-1]<=j):
                    arr2[i][j]=arr2[i-1][j-arr[i-1]] + arr2[i-1][j]  
            else:
                arr2[i][j]=arr2[i-1][j]       
    
    return arr2[n-1][m-1]
#__main__
arr=[2,3,5,6,8,10]
sum1=10
ans=dp(arr,sum1)
print(ans)