n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
sum_not_between=0
for num in arr:
    if num<a or num>b:
        sum_not_between+=num
print(sum_not_between)