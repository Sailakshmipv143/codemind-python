n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
l=[]
for i in range(m):
    s=0
    for j in range(n):
       s+=a[j][i]
    l.append(s)
print(*l)