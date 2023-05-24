n=int(input())
lst=list(map(int,input().split()))
for num in lst:
 if num%2!=0:
  res=num
print(res)