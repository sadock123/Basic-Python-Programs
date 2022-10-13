#main program
n=int(input('enter the number N'))
n1=1
n2=2
n3=n1+n2
sum=0
while (n3<n):
    n1=n2
    n2=n3
    n3=n1+n2
    print(n3)
    if (n3%2 == 0):
        sum = sum + n3
        
print(sum)