


Balance=1000

while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The available balance in your current account is:{Balance}")
    elif choice==2:
        amount=int(input("Enter amount to deposit:"))
        Balance+=amount
    elif choice==3:
        print("Enter how much amount you want to withdraw:")
        amount=int(input("Enter amount to withdraw:"))
        if amount<=Balance:
            Balance-=amount
        else:
            print("Invalid amount")
            print("please enter a sufficient amount in your balance")
    elif choice==4:
        print("Thank you for using ours services")
        print("I hope you enjoy your day")
        break
    else:
        print("Invalid choice")