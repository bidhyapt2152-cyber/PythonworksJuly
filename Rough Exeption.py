# Part A — raise (Easy)
# 1. Write a program to ask the user to enter a number. If the number is less than or equal to 0, raise a ValueError
# with the message "Number must be Positive".

# try:
#     n=int(input("Enter the number :"))
#
#     if n<=0:
#         raise ValueError("Number must be Positive")
#     else:
#         print(n)
#
# except ValueError as e:
#     print(e)

# 2. Ask the user to enter their age. If the age is less than 18, raise a ValueError with the message "Age must be 18
# or above".
# try:
#     age=int(input("Enter age :"))
#
#     if age<18:
#         raise ValueError("Age must be 18 or above")
#     else:
#         print(age)
#
# except ValueError as e:
#     print(e)

# 3. Ask the user to enter a mark. If the mark is greater than 100 or less than 0, raise a ValueError with the message
# "Invalid Mark".
# try:
#     mark=int(input("Enter mark :"))
#
#     if mark>100 or mark<0:
#         raise ValueError("Invalid Mark")
#     else:
#         print(mark)
#
# except ValueError as e:
#     print(e)
# # 4. Ask the user to enter a number. If the number is even, raise a ValueError with the message "Number must be Odd".
# try:
#     num=int(input("Enter the number :"))
#
#     if num%2==0:
#         raise ValueError("Number must be Odd")
#     else:
#         print(num)
# except ValueError as e:
#     print(e)

# Part B — as e
# 5. Write a program using try-except that raises:
# ValueError("Number must be Positive") and catches it using:
# # except ValueError as e:
# Print the error message using print(e).

# try:
#     num=int(input("Enter the number :"))
#
#     if num<=0:
#         raise ValueError("Number must be Positive")
#     else:
#         print(num)
#
# except ValueError as e:
#     print(e)




# 6. Ask the user to enter two numbers. If the second number is 0, raise a ValueError with the message ("Cannot divide"
# " by zero"). Handle it using as e.

# try:
#     num1= int(input("Enter the first number :"))
#     num2= int(input("Enter the second number :"))
#
#     if num2==0:
#         raise ValueError("Cannot divide by zero")
#
#
# except ValueError as e:
#     print(e)

# 7. Ask the user to enter a password. If its length is less than 8, raise a ValueError with a suitable message and
# print the message using as e.

# try:
#     password=input("Enter the password :")
#
#     if len(password)<8:
#         raise ValueError("Password must have atleast 8 characters")
#     else:
#         print(password)
#
# except ValueError as e:
#     print(e)

# Part C — Custom Exceptions
# 8. Create a custom exception called:
# InvalidPasswordError
# If the password length is less than 8, raise this exception with:
# Password should be 8 characters
# class InvalidPasswordError(Exception):
#     pass
# while True:
#     try:
#         password=input("Enter Password :")
#
#         if len(password)<8:
#             raise InvalidPasswordError("Password should be 8 characters")
#         else:
#             print("Password is correct")
#             break
#     except InvalidPasswordError as e:
#         print(e)


# 9. Create a custom exception called:
# InsufficientBalanceError
# Set:
# balance = 5000
# Ask the user to enter an amount. If the amount is greater than the balance, raise the custom exception with:
# Not Enough Balance. Transaction Failed
# class InsufficientBalanceError(Exception):
#     pass
# try:
#     balance=5000
#     amount=int(input("Enter Amount :"))
#
#     if amount>balance:
#         raise InsufficientBalanceError("Not Enough Balance. Transaction Failed")
#     else:
#         print("Transaction Sucess")
#
# except InsufficientBalanceError as e:
#     print(e)


# 10. Create a custom exception called:
# InvalidAgeError
# If age is less than 18, raise the exception with:
# Age must be 18 or above
# class InvalidAgeError(Exception):
#     pass
# try:
#     age=int(input("Enter Age :"))
#
#     if age<18:
#         raise InvalidAgeError("Age must be 18 or above")
#     else:
#         print(age)
#
# except InvalidAgeError as e:
#     print(e)

# 11. Create a custom exception called:
# InvalidMarkError
# If the mark is outside the range 0–100, raise the exception with:
# Mark should be between 0 and 100

# class InvalidMarkError(Exception):
#     pass
# try:
#     mark=int(input("Enter mark :"))
#
#     if mark not in range(0,100):
#         raise InvalidMarkError("Mark should be between 0 and 100")
#     else:
#         print("Mark -",mark)
#
# except InvalidMarkError as e:
#     print(e)


# Part D — while + Exception
# 12. Ask the user to enter a positive number. If the user enters 0 or a negative number, raise ValueError and ask
# again until a valid number is entered.
# while True:
#     try:
#         num=int(input("Enter a positive number :"))
#
#         if num<=0:
#             raise ValueError("Value must be positive")
#         else:
#             print(num)
#             break
#     except ValueError as e:
#         print(e)

# 13. Ask the user to enter a password. The password must contain at least 8 characters. Use a custom
# InvalidPasswordError and keep asking until the user enters a valid password.

# while True:
#     class InvalidPasswordError(Exception):
#         pass
#
#     try:
#         password=input("Enter password :")
#
#         if len(password)<8:
#             raise InvalidPasswordError("Password must contain at least 8 characters")
#         else:
#             print(password)
#             break
#     except InvalidPasswordError as e:
#         print(e)

# 14. Ask the user to enter an amount. Assume:
# balance = 10000
# If the amount is greater than the balance, raise InsufficientBalanceError and ask again until a valid amount is
# entered.
# while True:
#     class InsufficientBalanceError(Exception):
#         pass
#
#     try:
#         balance=10000
#         amount=int(input("Enter Amount :"))
#
#         if amount>balance:
#             raise InsufficientBalanceError("Insufficient Balance ")
#         else:
#             print(amount)
#             break
#     except InsufficientBalanceError as e:
#         print(e)


# 15. Ask the user to enter a number and calculate its factorial using math.factorial().
#     - Invalid input such as abc → handle ValueError
#     - Negative number → handle ValueError
#     - Keep asking until valid input is entered.
#
# while True:
#     try:
#         from math import factorial
#         num=int(input("Enter Number :"))
#
#
#         if num<=0:
#             raise ValueError("Value should be positive")
#
#         f = factorial(num)
#         print(f)
#         break
#     except ValueError as e:
#         print(e)




# 🔥 Part E — Exam-Level Mixed Questions
# 16. Write a program that asks for a username and password.
#     - Username cannot be empty.
#     - Password must contain at least 8 characters.
#     - Create a custom exception InvalidPasswordError.
#     - Use raise.
#     - Use except ... as e.
#     - Keep asking using a while loop until valid input is given.

# 17. Write a bank transaction program.
# balance = 5000
# Ask the user for an amount.
# - Amount must be positive.
# - Amount cannot be greater than balance.
# - Create InsufficientBalanceError.
# - Use raise.
# - Use as e.
# - Keep asking until a valid amount is entered.
# 18. Write a program that asks for a number and checks whether it is positive.
# Use:
# while True
# try
# raise
# except ... as e
# break
# The program should continue asking until the user enters a positive number.
# 19. Create two custom exceptions:
# InvalidAgeError
# InvalidMarkError
# Ask the user for age and mark.
# - Age < 18 → InvalidAgeError
# - Mark < 0 or mark > 100 → InvalidMarkError
# Handle both exceptions using as e.
# 20. Challenge: Write a program that asks for a password repeatedly.
# Requirements:
# - Password must be at least 8 characters.
# - Password must contain at least one digit.
# - Create a custom InvalidPasswordError.
# - Use raise.
# - Use except InvalidPasswordError as e.
# - Display the appropriate error message.
# - Continue asking until the password is valid.