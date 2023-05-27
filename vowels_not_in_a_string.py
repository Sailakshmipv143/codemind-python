n=input()
s=[]
x=['a','e','i','o','u']
for i in n:
    if i not in s and i in x:
        s.append(i)
if len(s)==5:
    print(0)
else:
    for i in x:
        if i not in s:
            print(i,end=" ")