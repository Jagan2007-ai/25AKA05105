


Questions={1:'''Question 1:
Which keyword is used to define a function in Python?

A. function
B. def
C. fun
D. define
''',2:'''Question 2:
Which data type is used to store multiple values in an ordered collection?
A. list
B. int
C. float
D. bool''',3:'''Question 3:
Which symbol is used to write a comment in Python?
A. //
B. /*
C. #
D. --''',4:'''Question 4:
What is the output of 5 + 3 * 2?
A. 16
B. 11
C. 13
D. 10''',5: """Question 5:
Which method adds an element to the end of a list?

A. add()
B. insert()
C. append()
D. push()
"""}

answers=['B','A','C','B',"C"]
user_answers=[]
count=1

def Quiz():
    global count
    count=1
    user_answers.clear()
    while count<=5:
        print(Questions[count])
        while True:
            answer=input("Enter your answer: ").strip().upper()
            if answer=="A" or answer =="B" or answer =="C" or answer =="D":
                user_answers.append(answer)
                count+=1
                break
            else:
                print("Enter a valid answer within(A,B,C,D)")
                print(Questions[count])


def Score():
    score=0
    for user_answer,answer in zip(user_answers,answers):
        if user_answer == answer:
            score=score+1
    return score



while True:
    print("*--------Menu--------*")
    print("1.Start Quiz")
    print("2.View Score")
    print("3.Exit")
    print("*--------Menu--------*")
    choice=int(input("Enter your choice: "))
    if choice==1:
        Quiz()
    elif choice==2:
        print(f"Your score is {Score()}")
    elif choice==3:
        print("Thanks for participating this quiz")
        break
    else:
        print("Enter a valid choice")




























