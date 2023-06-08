n=int(input())
arr=list(map(int,input().split()))
l=[]
s=0
for i in arr:
    if i not in l and i%2!=0:
        l.append(i)
        p=sum(l)
print(p)