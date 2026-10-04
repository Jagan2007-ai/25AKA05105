


books = {
    "PYTHONCRASHCOURSE": {
        "author": "Eric Matthes",
        "copies": 5
    },
    "CLEANCODE": {
        "author": "Robert C. Martin",
        "copies": 4
    },
    "HEADFIRSTJAVA": {
        "author": "Kathy Sierra & Bert Bates",
        "copies": 3
    },
    "THINKPYTHON": {
        "author": "Allen B. Downey",
        "copies": 5
    }
}
copies_track={"PYTHONCRASHCOURSE":0,"CLEANCODE":0,"HEADFIRSTJAVA":0,"THINKPYTHON":0}

def add_book():
    book_name = input("Please enter your book name: ").strip().upper().replace(" ","")
    if book_name in books:
            while True:
                copie = int(input("Please enter your copies: "))
                if copie>0:
                    books[book_name]["copies"] += copie
                    break
                else:
                    print("Your copies number should be positive")
    else:
        while True:
            author_name = input("Please enter the author name: ")
            copie = int(input("Please enter the number of copies: "))
            if copie>0:
                books[book_name]={'author': author_name, 'copies': copie}
                copies_track[book_name]=0
                break
            else:
                print("please enter a copies number should be positive")


def view_books():
    if not books:
        print("No books available")
        return
    else:
        print("Book Name\t\tAuthor Name\t\tCopies")
        for book in books:
            print(f"{book}\t{books[book]['author']}\t{books[book]['copies']}")


def search_book():
    book=input("Please enter your book name: ").strip().upper().replace(" ","")
    if book in books:
        print("Book found!")
        print(f"Book name: {book}")
        print(f"Author name: {books[book]['author']}")
        print(f"Available copies: {books[book]['copies']}")
    else:
        print("Book not found")

def issue_book():
    global copies_track
    book=input("please enter book name: ").strip().upper().replace(" ","")
    if book in books:
        if books[book]["copies"] == 0:
            print("Books are out of stack!")
        else:
            books[book]["copies"] -= 1
            copies_track[book] +=1
    else:
        print("Book not found")
def return_book():
    book=input('please enter book name; ').strip().upper().replace(" ","")
    if book in books:
        if copies_track[book]>0:
            books[book]["copies"] += 1
            copies_track[book] -=1
        else:
            print("Your returning book is already available")
            print("please enter a correct book name")
    else:
         print("Book not found")





while True:
    print("*-------Menu-------*")
    print("1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Issue Book")
    print("5.Return Book")
    print("6.Exit")
    print("*-------Menu-------*")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        break
    else:
        print("Enter a valid choice")

























