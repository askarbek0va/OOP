from amount import Amount
class PersonalAccount:

    def __init__(self, account_number, account_holder):
        self.__account_number=account_number
        self.__account_holder=account_holder
        self.__balance=0.0
        self.transactions=[]




    def deposit(self,amount):

        transaction = Amount(amount,'DEPOSIT')
        self.transactions.append(transaction)
        self.__balance = self.__balance + amount
        print('Deposit:', amount, ',Balance:', self.__balance)
        return

    def withdraw(self, amount):

        transaction = Amount(amount, 'WITHDRAWAL')
        self.transactions.append(transaction)
        if self.__balance >= amount:
           self.__balance -= amount
           print('Withdraw: ', amount, ',Balance:', self.__balance)
        else:
           print('Withdraw: ', amount, ', Not enough balance.')

    def print_transaction_history(self):
        if not self.transactions:
            print('No transactions to display')
            return

        print('Transaction history:')
        for transaction in self.transactions:
             print(transaction)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self,account_number):
        self.__account_number=account_number

    def get_account_holder(self):
        return self.__account_holder

    def set_account_holder(self,account_holder):
        self.__account_holder=account_holder

    def __str__(self):
        return f"Balance:{self.__balance}, Account number: {self.__account_number}, Account Holder: {self.__account_holder}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self,amount):
        self.withdraw(amount)
        return self



