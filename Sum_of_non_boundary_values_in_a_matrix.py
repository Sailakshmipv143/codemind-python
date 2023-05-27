n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
s=0
for i in range(1, n-1):
    for j in range(1, m-1):
        s+=a[i][j]
print(s)
