#
# try:
#     num1=int(input("Enter first number :"))
#     num2=int(input("Enter second number :"))
#     n=num1/num2
#     print("Result :",n)
#
# except ZeroDivisionError as e:
#     print(e)
#     print(type(e))
#
# except ValueError as e:
#     print(e)
#     print(type(e))
# except Exception as e:
#     print(e)
#     print(type(e))


#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

# try:
#     n=int(input("Enter number"))
#     if n<=0:
#         raise ValueError("Number must be Positive")
#     else:
#         print(n)
# except ValueError as e:                #works when "abc"typed
#     print(e)



#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")

# class InvalidPasswordError(Exception):
#     pass
#
# try:
#     p=input("Enter password :")
#     if len(p)<8:
#         raise InvalidPasswordError("Password should be 8 characters")
#     else:
#         print("password is correct")
#
# except InvalidPasswordError as e:
#     print(e)




#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class InsuffientBalanceError(Exception):
    pass

try:
    amount = int(input("Enter the Amount :"))
    balance=int(input("Enter tha Balance :"))

    if amount<balance:
        raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print(balance)

except InsuffientBalanceError as e:
    print(e)












