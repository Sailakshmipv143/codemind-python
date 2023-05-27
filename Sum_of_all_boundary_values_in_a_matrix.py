n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
s=0
for i in range(n):
    for j in range(m): 
        if i==0 or j==0 or i==n-1 or j==m-1:
           s+=a[i][j]
print(s)