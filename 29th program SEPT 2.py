# # # 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a
# # constructor by taking input from the user. Define the following methods:
# # #
# # # withdraw() – to withdraw an amount from the account and update the balance.
# # # deposit() – to deposit an amount into the account and update the balance.
# # # showbalance() – to display the current balance of the account.
# # #
# # # Create an object of the class and call the methods to perform withdrawal and deposit operations and display the
# # updated balance.
#
# class Account:
#     def __init__(self):
#
#         self.acctnumber = input("Enter Account Number: ")
#         self.acctname = input("Enter Account Holder Name: ")
#         self.balance = float(input("Enter Initial Balance: "))
#
#     def deposit(self):
#         amount = float(input("\nEnter amount to deposit: "))
#         if amount > 0:
#             self.balance += amount
#             print(f"Successfully deposited {amount}. Updated balance: {self.balance}")
#         else:
#             print("Invalid deposit amount!")
#
#     def withdraw(self):
#         amount = float(input("\nEnter amount to withdraw: "))
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Successfully withdrew {amount}. Updated balance: {self.balance}")
#         else:
#             print("Insufficient balance for withdrawal!")
#
#     def showbalance(self):
#         print(f"\nCurrent Balance for {self.acctname}: {self.balance}")
#
#
# acc1 = Account()
#
# acc1.showbalance()
#
# acc1.deposit()
#
# acc1.withdraw()
#
# acc1.showbalance()
#
# acc2 = Account()
#
# l=[acc1,acc2]
# for i in l:
#
#     i.showbalance()
#     #print(i.acctnumber,i.acctname,i.balance)
#
# acc2.showbalance()
#
# acc2.deposit()
#
# acc2.withdraw()
#
# acc2.showbalance()
#   #######################
#
# l=[acc1,acc2]
# for i in l:
#     if (i.acctnumber==123):
#         i.showbalance()
#
#
#           ########################################
#
#
# class Account:
#     # കൺസ്ട്രക്ടർ മെത്തേഡ് - അക്കൗണ്ട് വിവരങ്ങൾ നിർമ്മിക്കുന്നു
#     def __init__(self, acctnumber, acctname, initial_balance):
#         self.acctnumber = acctnumber
#         self.acctname = acctname
#         self.balance = float(initial_balance)
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Successfully deposited {amount}. Updated Balance: {self.balance}")
#         else:
#             print("Invalid deposit amount!")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Successfully withdrew {amount}. Updated Balance: {self.balance}")
#         else:
#             print("Insufficient balance!")
#
#     def showbalance(self):
#         print(f"\nAccount Number: {self.acctnumber}")
#         print(f"Account Holder: {self.acctname}")
#         print(f"Current Balance: {self.balance}")
#
#
# # എല്ലാ അക്കൗണ്ടുകളും സൂക്ഷിക്കാൻ ഒരു List ഉപയോഗിക്കുന്നു
# accounts_list = []
#
#
# # അക്കൗണ്ട് നമ്പർ ഉപയോഗിച്ച് ലിസ്റ്റിൽ നിന്നും ആ അക്കൗണ്ട് കണ്ടുപിടിക്കാനുള്ള ഫംഗ്ഷൻ
# def find_account(acc_num):
#     for account in accounts_list:
#         if account.acctnumber == acc_num:
#             return account
#     return None
#
#
# # MENU DRIVEN LOOP
# while True:
#     print("\n========== BANK OPERATIONS ==========")
#     print("1. Create a new Account")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Show Balance")
#     print("5. Exit")
#
#     ch = input("Enter your choice (1-5): ")
#
#     if ch == 1:
#         a=Account()
#         l.append(a)
#         print(l)
#
#     elif ch==2:
#         pass
#
#     elif ch==3:
#         pass
#     elif ch==4:
#         pass
#     else:
#         exit()


# Write a menu-driven Python program using a class Student
#     to perform the following operations:
# #
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student:
    def __init__(self, roll_no, name, mark):
        self.roll_no = roll_no
        self.name = name
        self.mark = mark

    def display_details(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Mark: {self.mark}")


# Global storage list for all student objects
student_list = []


# Helper function to look up an object by its unique roll number
def find_student(roll_no):
    for student in student_list:
        if student.roll_no == roll_no:
            return student
    return None


# MAIN MENU LOOP
while True:
    print("\n================ STUDENT DATABASE MENU ================")
    print("1. Add Student")
    print("2. Update Mark")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")
    print("=======================================================")

    choice = input("Enter your choice (1-6): ")

    # 1. ADD STUDENT
    if choice == '1':
        print("\n--- Add Student Record ---")
        try:
            r_no = int(input("Enter Roll Number: "))

            # Validation: Prevent duplication of Roll Numbers
            if find_student(r_no) is not None:
                print("Error: Student with this Roll Number already exists!")
            else:
                name = input("Enter Student Name: ")
                mark = float(input("Enter Marks: "))

                # Instantiate a new Student object and append it to the tracking list
                new_student = Student(r_no, name, mark)
                student_list.append(new_student)
                print("Success: Student record added successfully!")
        except ValueError:
            print("Invalid input! Roll Number must be an integer and Mark must be a number.")

    # 2. UPDATE MARK
    elif choice == '2':
        print("\n--- Update Mark ---")
        try:
            r_no = int(input("Enter Roll Number to update mark: "))
            student = find_student(r_no)

            if student is None:
                print("Result: Student not found!")
            else:
                new_mark = float(input(f"Enter new marks for {student.name}: "))
                student.mark = new_mark  # Directly updates data inside that object's box
                print("Success: Mark updated successfully!")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

    # 3. DISPLAY ALL DETAILS
    elif choice == '3':
        print("\n--- All Student Records ---")
        if not student_list:
            print("The database is currently empty.")
        else:
            for student in student_list:
                student.display_details()

    # 4. SEARCH STUDENT BY ROLL NUMBER
    elif choice == '4':
        print("\n--- Search Student ---")
        try:
            r_no = int(input("Enter Roll Number to search: "))
            student = find_student(r_no)

            if student is None:
                print("Result: Student not found!")
            else:
                print("Match Found:")
                student.display_details()
        except ValueError:
            print("Invalid Input! Roll number must be an integer.")

    # 5. DELETE STUDENT
    elif choice == '5':
        print("\n--- Delete Student ---")
        try:
            r_no = int(input("Enter Roll Number to delete: "))
            student = find_student(r_no)

            if student is None:
                print("Result: Student not found!")
            else:
                student_list.remove(student)  # Drops the object reference out of the list
                print(f"Success: Record of {student.name} deleted completely.")
        except ValueError:
            print("Invalid Input! Roll number must be an integer.")

    # 6. EXIT
    elif choice == '6':
        print("\nExiting Student Database System. Goodbye!")
        break

    else:
        print("Invalid Choice! Please enter a option between 1 and 6.")


