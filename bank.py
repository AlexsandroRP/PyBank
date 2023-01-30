import ast
from datetime import datetime
import pytz
from random import randint


class PyBank:  
    """
    Create an check account object to manage the customers accounts

    Attributes:
        Name (str): Customer name
        Id (str): Id customer
        Account (int)= Account customer
        Balance (float): Balance available
        Transactions (str): Transaction history
    """

    @staticmethod # -> Doesn't use any class information/methods
    def _date_time():
        zone = pytz.timezone('America/Chihuahua')
        time = datetime.now(zone)
        return time.strftime('%m/%d/%Y %H:%M:%S')

    def __init__(self, name, identification, account):  
        self.name = name # sinalizar para não alterar fora da classe
        self.id = identification # Indica ao usuário para não fazer mudança fora da classe
        self.balance = 10000
        self.account = account
        self.transactions = []
        

    def check_balance(self):
        print('Your current balancec is: U$ {:,.2f}'.format(self.balance))  

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((amount, f'Balance: {self.balance}', PyBank._date_time()))

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('You have insufficient funds to perform this transaction')
            self.check_balance()
        else:    
            self.balance -= amount
            self.transactions.append((-amount, f'Balance: {self.balance}', PyBank._date_time()))

    def check_transactions(self):
        print('Transaction history:')  
        print('Amount, Balance, Date and Time')
        for transaction in self.transactions:
            print(transaction)

    def transfer(self, amount, destination_account):
        if self.balance - amount < 0:
            print('You have insufficient funds to perform this transaction')
            self.check_balance()
        else:
            self.balance -= amount
            self.transactions.append((-amount, f'Balance: {self.balance}', PyBank._date_time()))
            destination_account.balance += amount
            destination_account.transactions.append((amount, destination_account.balance, PyBank._date_time()))

class CreditCard:

    @staticmethod # -> Doesn't use any class information/methods
    def _date_time():
        zone = pytz.timezone('America/Chihuahua')
        time = datetime.now(zone)
        return time

    def __init__(self, holder, checking_account): # qual conta faz parte
        self.number = randint(1000000000000000,9999999999999999)   
        self.holder = holder
        self.validity = '{}/{}'.format(CreditCard._date_time().month, CreditCard._date_time().year +4)
        self.cvc = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limit = 1000  
        self._password = '1234'
        self.checking_account = checking_account
        checking_account.cards.append(self) # pega o objeto cartão de crédito e adiciona dentro da lista de cartões, criando a relação entre as classes

    """
        Necessário quando algo pode ser mudado somente com alguma restrição
    """
    @property # Método GET | torna o método password um atributo
    def password(self): 
        return self._password

    @password.setter # Método SET | seta um método
    def password(self, value):
        if len(value) == 4 and value.isnumeric():
            self._password = value
        else:
            print('Invalid new password')

alex = PyBank('sadasasds', 151515, 1541541)
alex.check_balance()  

alex2 = PyBank('sadasasds', 151515, 1541541)
alex2.check_balance()  

alex.transfer(5000, alex2)
alex.check_balance()