n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
for i in l:
    if i>=a and i<=b:
        p.append(i)
if len(p)==0:
    print("-1")
else:
    print(max(p))