num=int(input())
sum_factors=0
for i in range(1,num):
  if num%i==0:
    sum_factors+=i
if sum_factors>num:
   print(True)
else:
   print(False)