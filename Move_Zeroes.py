n=int(input())
l=list(map(int,input().split()))
m=[]
n=[]
for e in l:
    if e==0:
        m.append(e)
    else:
        n.append(e)
print(*n+m)