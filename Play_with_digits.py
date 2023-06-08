def count(n):
    s=0
    while n:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
li=list(map(int,input().split()))
l=[]
for i in li:
    l.append(count(i))
print(sum(l))