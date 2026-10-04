


name=input("Enter student name: ")

Telugu=int(input("Enter Telugu marks: "))
English=int(input("Enter English marks: "))
Maths=int(input("Enter Maths marks: "))
Science=int(input("Enter Science marks: "))
Social=int(input("Enter Social marks: "))
Marks=(Telugu,English,Maths,Science,Social)
Total=0
count=0
for mark in Marks:
    Total+=mark
    count+=1

Average=Total/count

print(f"Student Name: {name}")
print(f"The total marks is: {Total}")
print(f"The average marks is: {Average}")
if 90<=Average<=100:
    print("Grade: A+")
elif 80<=Average<=89:
    print("Grade: A")
elif 70<=Average<=79:
    print("Grade: B")
elif 60<=Average<=69:
    print("Grade: C")
elif 50<=Average<=59:
    print("Grade: D")
else:
    print("Grade: F")


















