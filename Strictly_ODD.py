n=int(input())
l=[]
arr=list(map(int,input().split()))
c=0
for i in range (1,n,2):
    if arr[i]==0:
        continue
    if arr[i]%2!=0:
        continue
    print("False")
    break
else:
    print("True")
    
