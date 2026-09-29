# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input
# from the user. Define the following methods:
# #
# # getarea() – to calculate and display the area of the circle.
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# #
# # Create an object of the Circle class and call both methods to display the results.



#
# class Circle:
#     def __init__(self):
#
#         self.radius = float(input("Enter the radius of the circle: "))
#
#     def getarea(self):
#         # Area = π * r^2
#         area = 3.14 * (self.radius ** 2)
#         print(f"Area of the circle: {area:.2f}")
#
#     def getperimeter(self):
#
#         perimeter = 2 * 3.14 * self.radius
#         print(f"Perimeter of the circle: {perimeter:.2f}")
#
#
# c1 = Circle()
#
# c1.getarea()
# c1.getperimeter()



# # 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a
# constructor by taking input from the user. Define the following methods:
# #
# # withdraw() – to withdraw an amount from the account and update the balance.
# # deposit() – to deposit an amount into the account and update the balance.
# # showbalance() – to display the current balance of the account.
# #
# # Create an object of the class and call the methods to perform withdrawal and deposit operations and display the
# updated balance.

class Account:
    def __init__(self):
        
        self.acctnumber = input("Enter Account Number: ")
        self.acctname = input("Enter Account Holder Name: ")
        self.balance = float(input("Enter Initial Balance: "))

    def deposit(self):
        amount = float(input("\nEnter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. Updated balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self):
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Updated balance: {self.balance}")
        else:
            print("Insufficient balance for withdrawal!")

    def showbalance(self):
        print(f"\nCurrent Balance for {self.acctname}: {self.balance}")


acc = Account()


acc.showbalance()


acc.deposit()


acc.withdraw()


acc.showbalance()