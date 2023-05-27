n=int(input())
s=n*n
x=str(n)
y=str(s)
if y.endswith(x):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")