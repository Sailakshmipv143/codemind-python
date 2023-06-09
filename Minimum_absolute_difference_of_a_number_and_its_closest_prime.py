def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input())
if is_prime(n):
    print(0)
else:
    diff_greater=0
    diff_lesser=0
    greater=n
    lesser=n
    while True:
        greater+=1
        if is_prime(greater):
            diff_greater=greater-n
            break
    while True:
        lesser-=1
        if is_prime(lesser):
            diff_lesser=n-lesser
            break
    print(min(diff_greater,diff_lesser))