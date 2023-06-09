def is_prime(number):
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
def is_mega_prime(number):
    if not is_prime(number):
        return False
    digits=str(number)
    for digit in digits:
        if not is_prime(int(digit)):
            return False
    return True
num=int(input())
if is_mega_prime(num):
    print("Mega Prime")
else:
    print("Not Mega Prime")