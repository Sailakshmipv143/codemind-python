n=int(input())
arr=list(map(int,input().split()))
e=int(input())
c=0
for i in arr:
   if i==e:
    c=1
if c==1:
 print("True")
else:
 print("False")