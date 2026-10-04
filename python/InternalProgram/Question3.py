
start=int(input("Enter the first number"))
end=int(input("Enter the second number"))

for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)





















