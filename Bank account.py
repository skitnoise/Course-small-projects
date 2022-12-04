



class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance = 0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"{self.first_name}, {self.last_name}\nAccount balance {self.account_number}: ${self.balance}"

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print("Deposit accepted")


    def withdraw(self, amount_withdraw):
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print("Withdrawn done")
        else:
            print("Lack of funds")

def create_customer():
    first_name = input("Please, enter your first name:... ")
    last_name = input("Please, enter your last name:... ")
    account_number = input("Please, enter your account number:... ")
    client1 = Customer(first_name, last_name, account_number)
    return client1



def menu():
    my_customer = create_customer()
    print(my_customer)
    menu_choice = 0
    while menu_choice != 3:
        print(" [1] Do you want to deposit?\n"
              " [2] Do you want to withdraw?\n"
              " [3] Exit")
        menu_choice = int(input())
        if menu_choice == 1:
            dep_amount = int(input("Deposit amount:.. "))
            my_customer.deposit(dep_amount)
        elif menu_choice == 2:
            with_amount = int(input("Withdraw amount:..."))
            my_customer.withdraw(with_amount)
        print(my_customer)




    print("Thank you for using Python Bank")

menu()















