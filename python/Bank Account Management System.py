


accounts={
    1001:{
        'name': "kira",
        "balance":5000
    }
}




def create_account():
    while True:
        account_number=int(input("Enter account number: "))
        if account_number not in accounts:
            accounts[account_number]={}
            name=input("Enter your name: ")
            while True:
                amount=int(input("Enter amount: "))
                if amount>0:
                    accounts[account_number]['name']=name
                    accounts[account_number]['balance']=amount
                    break
                else:
                    print("The initial amount should be greater than 0")
            return
        else:
            print("Account already exists")

def view_account():
    while True:
        if not accounts:
            print("No accounts found!")
        else:
            for account_number in accounts:
                print(f"Account number: {account_number}")
                for key,value in accounts[account_number].items():
                    print(f'{key}: {value}')
            return

def search_account():
    while True:
        account_number=int(input("Enter account number to search: "))
        if account_number in accounts:
            print(f'account number: {account_number}')
            for key,value in accounts[account_number].items():
                print(f'{key} : {value}')
            return
        else:
            print("Account number not found")
def deposit_amount():
    while True:
        account_number = int(input("Enter account account number to deposit; "))
        if account_number in accounts:
            amount=int(input("Enter amount to deposit: "))
            if amount>0:
                print(f"old Balance: {accounts[account_number]['balance']}")
                accounts[account_number]['balance']+=amount
                print(f"Deposit amount: {amount}")
                print(f"New Balance: {accounts[account_number]['balance']}")
                return
            else:
                print('Deposit amount should be greater than 0')
        else:
            print("please enter a valid account number")
def withdraw_amount():
    while True:
        account_number = int(input("Enter account account number to withdraw; "))
        if account_number in accounts:
            while True:
                amount=int(input("Enter amount to withdraw: "))
                if amount>0 and amount<=accounts[account_number]['balance']:
                    print(f"Balance: {accounts[account_number]['balance']}")
                    accounts[account_number]['balance']-=amount
                    print(f"Withdraw amount: {amount}")
                    print(f"New Balance: {accounts[account_number]['balance']}")
                    break
                else:
                    print("Insufficient funds")
            return
        else:
            print("Account number not found")
def check_balance():
    while True:
        account_number = int(input("Enter account number to check Balance; "))
        if account_number in accounts:
            print(f"Account number: {account_number}")
            print(f'Holder name: {accounts[account_number]['name']}')
            print(f"current balance: {accounts[account_number]['balance']}")
            return
        else:
            print("Account number not found")
def delete_account():
    while True:
        account_number = int(input("Enter account number to delete; "))
        if account_number in accounts:
            accounts.pop(account_number)
            print("account Deleted successfully")
            return
        else:
            print("Account number not found")





while True:
    print(" ********** Bank Account Management System **********")
    print("1.create account")
    print("2.View Account")
    print("3.Search Account")
    print("4.Deposit Money")
    print("5.withdraw Money")
    print("6.Check Balance")
    print("7.Delete Account")
    print("8.Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        view_account()
    elif choice == 3:
        search_account()
    elif choice == 4:
        deposit_amount()
    elif choice == 5:
        withdraw_amount()
    elif choice == 6:
        check_balance()
    elif choice == 7:
        delete_account()
    elif choice == 8:
        print("Thanks for using our services")
        break
    else:
        print("Enter a valid choice")














