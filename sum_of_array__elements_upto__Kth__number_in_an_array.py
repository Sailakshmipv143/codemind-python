n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
l=[]
for i in arr:
    if i<=k:
        l.append(i)
print(sum(l))