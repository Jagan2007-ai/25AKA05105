
students = {
    101: {
        "name": "kira",
        "python": 90,
        "java": 85,
        "c": 88,
        "total":263,
        "average":87.66666666
    },
    102: {
        "name": "Priya",
        "python": 95,
        "java": 92,
        "c": 90,
        "total":277,
        "average":92.333333333
    }
}
def add_student():
    while True:
        marks={'python':0,'java':0,'c':0}
        roll_no=int(input("Enter roll no: "))
        total=0
        average=0
        if roll_no not in students:
            students[roll_no]={}
            name=input("Enter Student name: ")
            students[roll_no]['name'] = name
            for key,value in marks.items():
                while True:
                    print(f"Enter {key} marks: ",end=" ")
                    value = int(input())
                    if 0<=value<=100:
                        marks[key]=value
                        break
                    else:
                        print("Enter marks between 0 and 100")

            for key,value in marks.items():
                students[roll_no][key]=value
            for key, value in students[roll_no].items():
                if key != 'name':
                    print(f"{key} : {value}")
                    total = total + value
            students[roll_no]['total'] = total
            students[roll_no]['average'] = total/3
            return
        else:
            print("That roll no already exists")

def view_student():
    while True:
        if not students:
            print("No students")
        else:
            for roll in students:
                print(f"Roll no: {roll}")
                for key,value in students[roll].items():
                    if key != 'name':
                        print(f"{key} : {value}")
                    else:
                        print(f"{key} : {value}")
            return


def search_student():
    while True:
        roll=int(input("Enter roll no: "))
        if roll in students:
            print(f"Roll no: {roll}")
            for key, value in students[roll].items():
                if key != 'name':
                    print(f"{key} : {value}")
                else:
                    print(f"{key} : {value}")
            return
        else:
            print("That roll no does not exist")

def update_marks():
    while True:
        roll=int(input("Enter roll no: "))
        if roll in students:
            while True:
                for key in students[roll]:
                    if key != 'name' and key!='total' and key!='average':
                        print(f"{key}")
                subject=input("Enter subject name: ").lower()
                if subject=='python' or subject=='java' or subject=='c':
                    students['total']-=students[subject]
                    marks=int(input("Enter marks: "))
                    students[roll][subject]=marks
                    students[roll]['total']+=marks
                    students[roll]['average']=students[roll]['total']/3
                    break
                else:
                    print("That subject does not exist")
            return
        else:
            print("That roll no does not exist")

def delete_student():
    while True:
        roll=int(input("Enter roll no: "))
        if roll in students:
            students.pop(roll)
            return
        else:
            print("That roll no does not exist")

def view_topper():
    topper={}
    maximum=0
    if not students:
        print("No students")
    else:
        for roll in students:
             if students[roll]['total']>maximum:
                maximum=students[roll]['total']
                topper=students[roll]

        print("********* Topper *********")
        for key,value in topper.items():
            print(f"{key} : {value}")
    return



while True:
    print("****** Student Management System ******")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Marks")
    print("5.Delete Student")
    print("6.View Topper")
    print("7.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        view_topper()
    elif choice == 7:
        break
    else:
        print("That is not a valid choice")



















