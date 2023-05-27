n=input()
c=0
v='AEIOUaeiou'
for i in n:
    if i in v:
        c+=1
print(c)