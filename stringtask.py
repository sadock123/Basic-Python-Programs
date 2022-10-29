st=str(input())
vowel=["a","e","i","o","u","A","E","I","O","U","y","Y"]
s=''
for i in st:
    if i not in vowel:
        s=s+"."+i.lower()
print(s)