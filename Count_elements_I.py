n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
new=set(a)
new1=set(b)
p=new.intersection(new1)
print(len(p))