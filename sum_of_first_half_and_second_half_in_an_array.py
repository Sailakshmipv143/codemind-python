n=int(input())
l=list(map(int,input().split()))
p=0
k=0
for i in range(0,(n+2)//2):
    p+=i
for i in range(0,(n+1)):
    k+=i
print(p)
print(k-p)