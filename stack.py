
def push(num):
    s.append(num)
    return s
def poop():
    if s.isEmpty():
        return "stack is empty"
    else:
        s.remove()
def peek():
    if s.isEmpty():
        return "stack is empty"
    else:
        return s[-1]
       


#int main
s=[]
s.append(5)
print(s.pop())
s.append(8)
s.append(10)
s.peek()