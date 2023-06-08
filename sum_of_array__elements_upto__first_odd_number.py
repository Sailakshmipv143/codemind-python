n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(0,len(arr)):
    if arr[i]%2!=0:
        p=arr[i]
        break
    else:
        s+=arr[i]
print(s)