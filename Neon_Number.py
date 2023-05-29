n=int(input())
sqr=n*n
sumofdigits=0
while sqr>0:
    sumofdigits=sumofdigits+sqr%10
    sqr=sqr//10
if(n==sumofdigits):
    print("Neon Number")
else:
    print("Not Neon Number")