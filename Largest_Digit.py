n=int(input())
l=[]
while(n>0):
   r=n%10
   l.append(r)
   n=n//10
s=l[0]
for i in range(len(l)):
  if s<l[i]:
    s=l[i]
print(s)