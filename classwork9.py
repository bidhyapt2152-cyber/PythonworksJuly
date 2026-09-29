# Write a menu-driven Python program using a class Student to perform the following operations:
# #
# # 1Add Student(roll no,name,marks)
# # 2Update Marks
# # 3Display All Student Details
# # 4Search Student by Roll Number
# # 5Delete Student
# # 6Exit
# # Store student records in a list and perform all operations using the student's roll number.
#
#
# class Student:
#     def __init__(self):   ## init-initialize object
#         self.rollno=int(input("Enter roll number: "))
#         self.name =input("Enter name: ")
#         self.mark =int(input("Enter mark: "))
#
#     def updatemark(self):
#         self.mark=int(input("Enter new mark: "))
#
#     def details(self):
#         print("Roll number:",self.rollno)
#         print("Name:",self.name)
#         print("Mark:",self.mark)
#
# l=[]
# while(True):
#     print("Student details")
#     print("1.Add student")
#     print("2.Update mark")
#     print("3.Display all student details")
#     print("4.Search student by roll number")
#     print("5.Delete student")
#     print("6.Exit")
#     ch=int(input("Enter your choice: "))
#     if ch==1:
#         print("Add details- name,rollno,mark")
#         a=Student()
#         print(a)
#         l.append(a)
#     elif ch==2:
#         print("Update mark")
#         newroll= int(input("Enter roll number: "))
#         for i in l:
#             if i.rollno==newroll:
#                 i.updatemark()
#                 print("Mark updated successfully")
#                 break
#         else:
#             print("Student not found")
#
#     elif ch==3:
#         print("Display all students details")
#         for i in l:
#             i.details()
#             break
#         else:
#             print("No students found")
#     elif ch==4:
#         print("Search student by roll number")
#         num=int(input("Enter roll number: "))
#         for i in l:
#             if i.rollno==num:
#                 i.details()
#                 print("Student details found")
#                 break
#         else:
#             print("Roll number not found")
#     elif ch==5:
#         num=int(input("Enter roll number: "))
#         for i in l:
#             if i.rollno==num:
#                 l.remove(i)
#                 print("Student details deleted")
#                 break
#         else:
#             print("Student not found")
#
#     elif ch==6:
#         print("Existing....")
#         exit()