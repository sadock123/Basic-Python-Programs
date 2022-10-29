t=int(input())
while (t>0):
    n=int(input())
    code=input()
    res=""
    while code:
        if code[-1] != '0':
            res = chr(96 + int(code[-1])) + res
            code = code[:-1]
        else:
            res = chr(96 + int(code[-3:-1])) + res
            code = code[:-3]
    print(res)
    t-=1