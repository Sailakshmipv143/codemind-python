n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
list=[]
for i in l:
    if i<a or i>b:
        list.append(i)
if len(list)==0:
    print("-1")
else:
    m=max(list)
    print(m)