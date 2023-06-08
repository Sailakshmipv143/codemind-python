b,c=map(int,input().split())
s=list(map(int,input().split()))
co=0
j,k=[],[]
for i in s:
    j.append(abs(i))
for l in j:
    k.append(str(l))
for h in k:
    if len(h)==c:
        co+=1
    else:
        pass
print(co)