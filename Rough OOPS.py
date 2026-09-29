# Level 1 — Class & Object
# 1. Student Class
# Create a Student class with:
# - name
# - age
# - course
# Create an object and display all the details.
# Expected output:
# Name: Bidhya
# Age: 22
# Course: Python
# 2. Employee Class
# Create an Employee class with:
# - employee name
# - employee ID
# - salary
# Create an object and display the details.
# 3. Rectangle
# Create a Rectangle class with:
# - length
# - breadth
# Create methods to calculate:
# - Area
# - Perimeter
# 🟢 Level 2 — __init__() and self
# 4. Bank Account
# Create a BankAccount class with:
# - account holder name
# - account number
# - balance
# Use __init__() to initialize the values.
# Create a method:
# display()
# to display the account details.
# 5. Product
# Create a Product class with:
# - product name
# - price
# - quantity
# Create a method to calculate:
# total = price × quantity
# Display the total price.
# 6. Calculator
# Create a Calculator class with methods:
# add()
# subtract()
# multiply()
# divide()
# Take two numbers from the user and perform the operations.
# 🟡 Level 3 — Inheritance
# 7. Single Inheritance
# Create:
# Person
#    ↓
# Student
# Person should contain:
# name
# age
# Student should contain:
# course
# Display all three details.
# 8. Employee → Manager
# Create an Employee class with:
# name
# salary
# Create a Manager class that inherits from Employee and adds:
# department
# Display all details.
# 🟡 Level 4 — Method Overriding
# 9. Animal Sounds
# Create a parent class:
# Animal
# with:
# sound()
# Create child classes:
# Dog
# Cat
# Cow
# Override sound() in each class.
# Expected:
# Dog barks
# Cat meows
# Cow moos
# 10. Vehicle
# Create a parent class Vehicle with:
# start()
# Create child classes:
# Car
# Bike
# Override start() so that:
# Car → Car starts
# Bike → Bike starts
# 🟡 Level 5 — super()
# 11. Parent + Child Method
# Create:
# class Parent:
#     def show(self):
#         print("Parent")
# Create a Child class that overrides show().
# Use super() so that the output is:
# Parent
# Child
# 12. Person → Student
# Person should have:
# display()
# that prints:
# I am a person
# Student should override display() but use super() first.
# Expected:
# I am a person
# I am a student
# 🟠 Level 6 — Method Overloading Concept
# 13. Calculator with Different Arguments
# Create a Calculator class with an add() method that can accept:
# 2 numbers
# 3 numbers
# For example:
# c.add(10, 20)
# c.add(10, 20, 30)
# Expected:
# 30
# 60
# 💡 Hint: Python doesn't support traditional method overloading. Use a default argument or *args.
# 🟠 Level 7 — Abstraction
# 14. Animal Abstract Class
# Create an abstract class:
# Animal
# with an abstract method:
# sound()
# Create:
# Dog
# Cat
# and implement sound() in both.
# Expected:
# Dog barks
# Cat meows
# 15. Shape Abstract Class ⭐
# Create an abstract class Shape with:
# area()
# Create child classes:
# Circle
# Rectangle
# Implement area() differently in each class.
# 🔴 Level 8 — OOP + Exception Handling
# 16. Bank Account ⭐
# Create a BankAccount class with:
# deposit()
# withdraw()
# Handle these situations:
# - Deposit amount must be positive.
# - Withdrawal amount must be positive.
# - Withdrawal amount cannot exceed balance.
# Use try-except to handle invalid input.
# 17. Calculator with Exception Handling ⭐
# Create a Calculator class that performs division.
# Handle:
# - ValueError
# - ZeroDivisionError
# Example:
# Enter first number: 10
# Enter second number: 0
#
# Cannot divide by zero
# 🔥 Exam-Level Questions
# 18. Employee Management
# Create an Employee class with:
# employee_id
# name
# designation
# salary
# Create methods:
# display()
# update_salary()
# Allow the user to update the salary and display the updated details.
# 19. Student Result System
# Create a Student class with:
# name
# roll_no
# mark1
# mark2
# mark3
# Create methods to:
# - Calculate total
# - Calculate average
# - Display grade
# Use appropriate OOP concepts.
# 20. ⭐ Combined OOP Question
# Create an abstract class Vehicle with an abstract method:
# start()
# Create two child classes:
# Car
# Bike
# Each child should implement start() differently.
# Also create a normal method in Vehicle:
# display()
# which prints:
# This is a vehicle
# Use super() from the child class where appropriate.