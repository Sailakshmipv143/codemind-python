n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in arr:
    if i>=a and i<=b:
        l.append(i)
print(sum(l))