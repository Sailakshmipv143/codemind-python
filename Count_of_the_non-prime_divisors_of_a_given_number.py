def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input())
non_prime_divisors=0
for i in range(1,n+1):
    if n%i==0 and not is_prime(i):
        non_prime_divisors+=1
print(non_prime_divisors)