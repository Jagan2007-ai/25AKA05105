


def MultipleReturn(a,b):
    return a+b,a-b,a*b,a/b


a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
sums,sub,mul,div=MultipleReturn(a,b)

print(f"The sum of {a} and {b} is {sums}")
print(f"The subtraction of {a} and {b} is {sub}")
print(f"The multiplication of {a} and {b} is {mul}")
print(f"The division of {a} and {b} is {div}")





























