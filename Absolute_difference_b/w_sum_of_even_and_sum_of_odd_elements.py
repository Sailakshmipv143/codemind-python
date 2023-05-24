n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in arr:
 if i%2==0:
   es=es+i
 else:
  os=os+i
print(abs(es-os))