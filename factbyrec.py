def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

m=int(input("enter a number"))
print("the factorial of n is",factorial(m))

