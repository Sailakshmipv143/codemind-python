n=int(input())
l=[]
c=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2==0:
        l.append(i)
        c+=1
if c==n:
    print("True")
else:
    print("False")