'''
Instructions:

Please extend the Account, Bank and Customer classes located in bank.py (https://github.com/prubach/Python_Summer_2021_2/blob/master/bank/Bank.py) filling in the TODOs and adding:
- validation for deposit to prevent any misuse of this function (unsafe operations that can influence the balance of the acoount
- implementation of the list of Customers and Accounts in Bank. Use a single list for both types of accounts. Use the factory methods that create Customer and XXXAccount objects to add the pointers to those newly created objects to the appropriate list.
- implementation of transfer(...) in Bank. As you do that please also include validation of input parameters
'''

class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(
            self.customer_id) + "): " + self.first_name + " " + self.last_name + " (" + self.email + ")"


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self.__balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        if amount < 0:
            print('Cannot add negative funds: ' + str(amount))
            # alternatively
            # self.charge(-amount)
        else:
            self.__balance += amount
            print("Deposited: " + str(amount) + " to account[" + str(self.account_id) + "]. New balance: " + str(self.__balance))

    def charge(self, amount):
        if amount < 0:
            print('Cannot withdraw less than 0: ' + str(amount))
            # alternatively
            # self.deposit(-amount)
        elif self.__balance >= amount:
            self.__balance -= amount
            print("Charged: " + str(amount) + " from account[" + str(self.account_id) + "]. New balance: " + str(self.__balance))
        else:
            print("Sorry, you do not have that much money on your account to withdraw: " + str(amount))

    def calc_interest(self, a=1):
        # a is number of growth periods in a year, default is 1
        return self.__balance * (1 + self.interest_rate/a) ** a - self.__balance

    def get_balance(self):
        return self.__balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4}".format(self.__class__.__name__, self.account_id, self.__balance,
                                                             self.customer.first_name, self.customer.last_name)


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_id_from, acc_id_to, amount):
        self.accounts[acc_id_from - 1].charge(amount)
        self.accounts[acc_id_to - 1].deposit(amount)

    def __repr__(self):
        return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)


bank = Bank()

c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
c2 = bank.create_customer("Mark", "Powerrade", "makeyoufly@gmail.com")
print(c1)
print(c2)
a1 = bank.create_account(c1)
a2 = bank.create_account(c2)
print(a1)
print(a2)
a1.deposit(230)
a1.deposit(-10)
a1.charge(100)
a1.charge(-100)

print(bank)

print('')
a1.__balance = 55
print(a1.get_balance())
print(a1.calc_interest())

print('')
bank.transfer(1, 2, -50)
print('')
bank.transfer(1, 2, -50)