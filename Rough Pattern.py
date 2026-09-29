#Right Triangle
# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print("*",end="")
#         else:
#             print("", end="")
#     print()

def right(s):
    for i in range(s):
        for j in range(s):
            if j<=i:
                print("*",end=" ")
            else:
                print("",end=" ")
        print()

right(4)


#Hollow Square
#
# for i in range(7):
#     for j in range(7):
#         if i==0 or i==7-1 or j==0 or j==7-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
#
# for i in range(7):
#     for j in range(7):
#         if i==0 or i==7-1 or j==0 or j==7-1:
#             print("* ", end="") # Added a space after the asterisk
#         else:
#             print("  ", end="") # Added a second space to match character width
#     print() # Indented this line to move to the next row
#
# def print_hollow_square(size):
#     # Outer loop for rows
#     for i in range(size):
#         # Inner loop for columns
#         for j in range(size):
#             # Print '*' for the borders (first/last row or first/last column)
#             if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#                 print("*", end=" ")
#             else:
#                 # Print space for the hollow inner part
#                 print(" ", end=" ")
#         # Move to the next line after completing a row
#         print()
#
# print_hollow_square(5)


