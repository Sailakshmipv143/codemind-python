n=int(input())
array=list(map(int,input().split()))
average=sum(array)//n
is_present=average in array
print(is_present)