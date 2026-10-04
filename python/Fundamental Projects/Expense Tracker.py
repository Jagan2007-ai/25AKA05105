


Expenses_names=[]
Expenses_amounts=[]
Total_Expenses=0

while True:
    print("-------**Menu List**--------")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Total Expenses")
    print("4.Exit")
    print("-------********--------")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter Expense name: ")
        amount=int(input("Enter Expense amount(Dollars): "))
        if amount>0:
            Expenses_amounts.append(amount)
            Total_Expenses = Total_Expenses + amount
            Expenses_names.append(name)
        else:
            print("Amount must be greater than 0")
    elif choice==2:
        if not Expenses_names and  not Expenses_amounts:
            print("Expenses are empty")
        else:
            for name,amount in zip(Expenses_names,Expenses_amounts):
                print(f"{name} : {amount}")
    elif choice==3:
        print(f'Total Expenses: ${Total_Expenses}')
    elif choice==4:
        print("Thanks for using our services")
        print("Goodbye")
        break
    else:
        print("Invalid choice")


























