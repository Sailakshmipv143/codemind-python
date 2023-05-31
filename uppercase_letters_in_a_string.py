s=input()
c=0
for i in s:
    if ord(i) in range(65,91):
        c+=1
print(c)