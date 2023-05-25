n,m=map(int,input().split())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
e=0
o=0
for i in range(n):
   for j in range(m):
       if a[i][j]%2==0:
           e+=a[i][j]
       else:
           o+=a[i][j]
print(e,o)