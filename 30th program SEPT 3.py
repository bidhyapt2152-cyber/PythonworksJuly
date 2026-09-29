# INHERITANCE

class Parent:
    def m1(self):
        print("In parent class method m1")

    def m2(self):
        print("In parent class method m1")
#
# p=Parent
# p.m1()
# p.m2()

# class Child(Parent):
#     pass
# c=Child()
#
# c.m1()
# c.m2()

   #child has its own properties.
#
# class Child(Parent):
#     def m3(self):
#         print("In child class method m3")
# c=Child()
#
# c.m1()
# c.m2()
# c.m3()

   # to change m1 by child

# class Child(Parent):
#
#     def m1(self):
#         print("In child class m1")
#
#     def m3(self):
#
#         print("In child class method m3")
# c=Child()
#
# c.m1()
# c.m2()
# c.m3()


# to acces m1 by child also can change its content
# class Child(Parent):
#
#     def m1(self):      # to bring attributes from parent
#         super().m1()
#         print("In child class m1")
#
#     def m3(self):
#         print("In child class method m3")
#
#
# c = Child()
#
# c.m1()
# c.m2()
# c.m3()


               ###################
#initialization code

# class Person:
#     def __init__(self):
#         self.name=input("Enter Name :")
#         self.age=int(input("Enter Age :"))
#
#     def show(self):
#         print(self.name,self.age)
#
# # i)
#
# class Student(Person):             #go to parent init function
#     pass
#
# s=Student()

# ii)

# class Student(Person):             #go to child init function
#     def __init__(self):
#         self.rollno=int(input("Enter Roll.no :"))
#         self.course=input("Enter Course :")
#         self.mark=int(input("Enter Mark :"))
#
#
#
# s=Student()


# iii)

# class Student(Person):             #go to parent init function along with child init fun
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter Roll.no :"))
#         self.course=input("Enter Course :")
#         self.mark=int(input("Enter Mark :"))
#
#
#
# s=Student()


# iv)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter Roll.no :"))
#         self.course=input("Enter Course :")
#         self.mark=int(input("Enter Mark :"))
#
#     def show(self):
#         super().show()
#         print(self.rollno,self.course,self.mark)
#
#
#
#
# s=Student()
# s.show()


# iv)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter Roll.no :"))
#         self.course=input("Enter Course :")
#         self.mark=int(input("Enter Mark :"))
#
#     def show(self):
#         super().show()
#         print(self.rollno,self.course,self.mark)
#
#     def updatemark(self):
#         self.mark=int(input("Enter Mark :"))
#
#
# s=Student()
# s.show()
# s.updatemark()
# s.show()

              ##################################

# #company
#
# class Company:                                                                      #company
#
#     def __init__(self):
#         self.name=input("Enter Company Name :")
#         self.location=input("Enter Location :")
#
#     def display_company(self):
#         print(self.name,self.location)
#
# class Employee(Company):                                                                      #employee
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("Enter Employer ID :"))
#         self.name=input("Enter Employer Name :")
#         self.designation=input("Enter designation :")
#         self.salary=int(input("Enter Salary :"))
#
#     def display_details(self):
#         super().display_company()
#         print(self.empid,self.name,self.designation,self.salary)
#
#
#     def update_salary(self):                                               #update salary
#
#         self.salary=round(self.salary*1.1)                          #Mathematically it is 110.
#                                                              #But Python uses floating-point numbers to store decimal
#                                                               # values such as 1.1, and sometimes they cannot be
#                                                               # representedperfectly in binary.
#         print("Salary updated sucessfully")



# e=Employee()
# e.display_company()
# e.update_salary()
# e.display_details()

#Category

class Category:                                                         #product
    def __init__(self):
        self.category_name=input("Enter category : ")

    def show_category(self):
        print("Category",self.category_name)



#Product
class Product(Category):

    def __init__(self):
        super().__init__()
        self.product_name=input("Enter Product Name :")
        self.price=int(input("Enter Price :"))
        self.Quantity=int(input("Enter Quantity :"))

    def total_price(self):
        print("Total product price =",self.price*self.Quantity)

p=Product()
p.total_price()





