num=int(input())
s=0
num_str=str(num)
for i in range(len(num_str)):
    s+=int(num_str[i])**(i+1)
if s==num:
    print(True)
else:
    print(False)