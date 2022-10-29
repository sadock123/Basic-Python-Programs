
n=int(input())
count=0
while (n):
    
    cat=str(input())
    if (cat=="Tetrahedron"):
        count=count+4
    elif (cat=="Cube"):
        count=count+6
    elif (cat=="Octahedron"):
        count=count+8
    elif (cat=="Dodecahedron"):
        count=count+12
    elif (cat=="Icosahedron"):
        count=count+20
    n=n-1
print(count)

   
    
