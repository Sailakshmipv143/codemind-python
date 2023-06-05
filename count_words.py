s=input().split()
c=0
v="aeiou"
cons="bcdfghjklmnpqrstvwxyz"
for word in s:
    if word[0].lower() in v and word[-1][-1].lower() in cons:
        c+=1
print(c)