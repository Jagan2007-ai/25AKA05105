


contact_book={}

def add_contact(name,number):
    contact_book[name]=number

def view_contact():
    if not contact_book:
        print("no contacts found")
    else:
        print("The contact list is:")
        for key,value in contact_book.items():
            print(f"{key}-{value}")


def search_contact(name):
    if name in contact_book:
        print(f"{name}-{contact_book.get(name)}")
    else:
        print("no contact found")

def remove_contact(name):
    if name in contact_book:
        contact_book.pop(name)
    else:
        print("No contact found to remove")

while True:
    print("*-----Detials--------*")
    print("1.Add contact")
    print("2.View contact")
    print("3.Search contact")
    print("4.Remove contact")
    print("5.Exit")
    print("*-------Detials--------*")
    choice=int(input("Enter your choice:"))
    if choice ==1:
        name = input("Enter contact name:")
        number =input("Enter contact number(+91):")
        if len(number)==10:
            add_contact(name,number)
        else:
            print("The number should contain 10 numbers!)")
    elif choice ==2:
        view_contact()
    elif choice ==3:
        name=input("Enter contact name:")
        search_contact(name)
    elif choice ==4:
        name=input("Enter contact name:")
        remove_contact(name)
    elif choice ==5:
        print("Exiting...")
        break
    else:
        print("Enter a valid choice(1 to 5)")
































