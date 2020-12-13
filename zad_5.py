from typing import List


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
        self._balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount has to be numerical value.")
        self._balance += amount
        print("Deposited: " + str(amount) + ". The new balance is: " + str(self._balance))

    def charge(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount has to be numerical value.")
        if self._balance >= amount:
            self._balance -= amount
            print("Charged: " + str(amount) + ". The new balance is: " + str(self._balance))
        else:
            print("Sorry, you do not have that much money on your account to withdraw: " + amount)

    def calc_interest(self):
        self._balance *= (1 + self.interest_rate)

    def get_balance(self):
        print("The balance is: " + str(self._balance))
        return self._balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4} ".format(self.__class__.__name__, self.account_id, self._balance,
                                                              self.customer.first_name, self.customer.last_name)
        # return self.__class__.__name__ + "(" +  + ")" + " belonging to: " + self.customer.first_name + " " + self.customer.last_name  + " (" + self.customer.email + ")"


class Bank:
    def __init__(self):
        self.customers: List[Customer] = []
        self.accounts: List[Account] = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_id_from, acc_id_to, amount):
        if not isinstance(acc_id_from, int) or not isinstance(acc_id_from, int):
            raise TypeError("Ids must be expressed in ints.")

        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount has to be numerical value.")

        if amount < 0:
            raise ValueError("Transfer has to be positive")

        from_account = [account for account in self.accounts if account.account_id == acc_id_from]
        if len(from_account) != 1:
            raise ValueError("Account with given id does not exist.")
        from_account = from_account[0]

        to_account = [account for account in self.accounts if account.account_id == acc_id_to]
        if len(to_account) != 1:
            raise ValueError("Account with given id does not exist.")
        to_account = to_account[0]

        from_account.charge(amount=amount)
        to_account.deposit(amount=amount)

    def __repr__(self):
        return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)


bank = Bank()

c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
print(c1)
a1 = bank.create_account(c1)
print(a1)
a1.deposit(200)
a1.charge(100)

print(bank)

# testing transfer

c2 = bank.create_customer("Joanna", "Kowalski", "jo.kowalski@gmail.com")
a2 = bank.create_account(c2)
a2.deposit(500)

a1_before = a1.get_balance()
a2_before = a2.get_balance()

transfer_amount = 10

bank.transfer(acc_id_from=a1.account_id, acc_id_to=a2.account_id, amount=transfer_amount)

assert a1_before - transfer_amount == a1.get_balance()
assert a2_before + transfer_amount == a2.get_balance()

# testing calc_interest

a1_before = a1.get_balance()

a1.calc_interest()

assert a1.get_balance() == a1_before + a1_before * a1.interest_rate
