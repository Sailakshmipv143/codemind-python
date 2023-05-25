num=int(input())
sum=0
num_str=str(num)
for i in range(len(num_str)):
    sum+=int(num_str[i])**(i+1)
if sum==num:
   print(True)
else:
   print(False)