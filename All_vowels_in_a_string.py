s=input()
l=list(s)
v="aeiou"
lst=[]
for i in l:
    if i in v and i not in lst:
        lst.append(i)
if len(lst)==5:
    print("True")
else:
    print("False")