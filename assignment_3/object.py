from personal_account import PersonalAccount

if __name__=='__main__':
    account = PersonalAccount(int(input('Please enter your account number:')), input('Please enter your account holder:'))
    print(account)

    account.deposit(float(input('\nAmount of deposit: ')))
    account.withdraw((float(input('\nAmount of withdrawal:'))))
    account.withdraw((float(input('\nAmount of withdrawal:'))))

    account.print_transaction_history()

    print(f'\n Current Balance: {account.get_balance()}')

    account + float(input('\namount of deposit: '))
    account - float(input('\namount of deposit: '))

    print(account)

