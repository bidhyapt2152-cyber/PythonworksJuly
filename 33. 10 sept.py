#using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math
while(True):
    try:
        n=int(input("enter the number:"))
        m=math.factorial(n)
        print("factorial",m)
        break
    except ValueError:
        print("Value Error")
    except:
        print("Error")


 ###################################

# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
#
# while (True):
#     print("simple calculator")
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.multiplication")
#     print("4.Division")
#     print("5.Exit")
#
#     try:
#         ch=int(input("enter the choice:"))
#         if ch==1:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             sum=n1+n2
#             print("sum:",sum)
#
#         elif ch==2:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             diff=n1-n2
#             print("difference:",diff)
#
#         elif ch==3:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             mul=n1*n2
#             print("multiplication:",mul)
#
#         elif ch==4:
#              n1=int(input("enter the number1:"))
#              n2=int(input("enter the number2:"))
#              div=n1/n2
#              print("division:",div)
#
#         elif ch==5:
#              print("exit")
#              break
#
#         else:
#             print("invalid choice")
#     except ValueError:
#        print("ValueError")
#     except ZeroDivisionError:
#         print("Zero division error")
#     except:
#         print("error")

          ##############################

 #write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#     fn=input("enter the file name:")
#     f=open(fn,"r")
#     print("file opened successfully")
# except FileNotFoundError:
#     print("File not found")

     #################################
#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
try:
    d={"name":"arun","age":23,"place":"ekm"}
    n=input("enter the key value:")
    print(d[n])


except KeyError:
    print("KeyError")


        ###############################

