from personal_account import PersonalAccount

if __name__=='__main__':
    account = PersonalAccount(int(input('Please enter your account number:')), input('Please enter your account holder:'))
    print(account)

    account.deposit(float(input('\nAmount of deposit:')))
    account.withdraw((float(input('\nAmount of withdrawal:'))))
    account.withdraw((float(input('\nAmount of withdrawal:'))))

    account.print_transaction_history()

    print(f'\nCurrent Balance: {account.get_balance()}')

    account + int(input('\namount of deposit: '))  # Using __add__ to deposit
    account - int(input('\namount of withdrawal: '))  # Using __sub__ to withdraw
    print(account)

