n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
  if list[i]!=0:
    c=i
print(c)