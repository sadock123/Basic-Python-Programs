l=[]
for i in range(3):
    l.append(int(input()))

a=l[0]
b=l[1]
c=l[2]
print(max((a*b*c),(a+b+c),((a+b)*c), a*(b+c)))