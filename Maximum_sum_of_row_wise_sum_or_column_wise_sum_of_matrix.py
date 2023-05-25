n,m=map(int,input().split())
a=[]
for i in range(n):
   row=list(map(int,input().split()))
   a.append(row)
l=[]
for i in range(n):
    l.append(sum(a[i]))
print(max(l))