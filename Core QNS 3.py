# 🔥 Lambda / Higher Order Function Questions

# Q15. Filter and Transform
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter() and map(), produce the squares of only the even numbers.
# Expected:
# [4, 16, 36, 64, 100]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even=filter(lambda n: n%2==0,numbers)
# sq=map(lambda s:s**2,even)
# print(list(sq))



# ________________________________________
# Q16. Filter Names
# Given:
# names = ["Anu", "Anjali", "Arun", "Akhil", "Binu", "Amal"]
# Using filter() and lambda, return names that:
# •	start with "A"
# •	and have more than 4 characters.
# Expected:
# ['Anjali', 'Akhil']
# #
# names = ["Anu", "Anjali", "Arun", "Akhil", "Binu", "Amal"]
# print(list(filter(lambda n:n[0]=="A" and len(n)>4,names)))


# ________________________________________
# Q17. Reduce — Largest Number
# Using reduce() and lambda, find the largest number from:
# numbers = [12, 45, 7, 89, 34, 23]
# Expected:
# 89
# numbers = [12, 45, 7, 89, 34, 23]
# from functools import reduce
# print(reduce(lambda a,b:a if a>b else b,numbers))


# ________________________________________
# Q18. Reduce — Product
# Using reduce() and lambda, calculate the product of all numbers in a list.
# Input: [2, 3, 4, 5]
# Output: 120
# l=[2, 3, 4, 5]
# from functools import reduce
# print(reduce(lambda a,b:a*b,l))

# ________________________________________
# 🧠 Logic-Based Questions
# These are closer to the kind of questions where you have to figure out the approach yourself.

# Q19. Number Frequency Without Dictionary
# Write a program to find the most frequently occurring number in a list without using a dictionary.
# Input:
# [3, 5, 3, 2, 5, 3, 8, 5]
#
# Output:
# 3
# l=[3, 5, 3, 2, 5, 3, 8, 5]
# count=0
# for i in l:
#     if l.count(i)>count:
#         count=l.count(i)
#
# print(count)

# ________________________________________
# Q20. Consecutive Numbers
# Write a program to find the longest sequence of consecutive numbers in a list.
# Input:
# [100, 4, 200, 1, 3, 2]
#
# Output:
# 4
#
# Explanation:
# 1, 2, 3, 4 → 4 consecutive numbers
# l=[100, 4, 200, 1, 3, 2]
# s=set(l)
# maximum=0
#
# for i in s:
#     if i-1 not in s:
#         count=1
#         current=i
#         while current+1 in s:
#             current+=1
#             count+=1
#
#         if count>maximum:
#             maximum=count
#
# print(maximum)



# ________________________________________
#
#
# SET 4
#
# 🔥 Pattern Questions — Actual Logic Style
# Q21.
# For n = 5, print:
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# ________________________________________
# Q22.
# For n = 5:
# 1
# 22
# 333
# 4444
# 55555
# Try solving using a single outer loop and string repetition.
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
# ________________________________________
# Q23.
# Print:
# 1
# 23
# 456
# 78910
# For n = 4.
# The numbers should continue increasing rather than restarting from 1 on every row.
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=1
#     print()

# ________________________________________
# Q24.
# For n = 5:
#     1
#    121
#   12321
#  1234321
# 123454321


# Total number of rows




# for i in range(1,6):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()
#
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()
# for i in range(1,6):
#     print(" "* (5-i),end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()


# for i in range(1,6):
#     print(" "*(5-i),end="")
#
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# ________________________________________
# 🧩 Mixed Questions
# Q25. Student Marks
# Write a function:
# student_result(marks)
# that accepts a list of marks and returns:
# •	highest mark
# •	lowest mark
# •	average
# •	number of students who passed
# Passing mark = 40.
# Example:
# Input: [35, 78, 45, 90, 22, 56]
#
# Output:
# Highest: 90
# Lowest: 22
# Average: ...
# Passed: 4
#
# def student_result(marks):
#     h=0
#     l=float("inf")
#     for i in marks:
#         if i>h:
#             h=i
#
#     print("Highest :",h)
#
#     for i in marks:
#         if i<l:
#             l=i
#     print("Lowest:",l)
#
#     s=0
#     for i in marks:
#         s+=i
#         avg=s/len(marks)
#
#     print("Average:",avg)
#
#     Passing_mark=40
#     count=0
#     for i in marks:
#         if i>=40:
#             count+=1
#
#     print("Passed :",count)
#
#     return
# lst=[35, 78, 45, 90, 22, 56]
# student_result(lst)



# ________________________________________
# Q26. Shopping Cart
# Given:
# cart = [
#     ("Pen", 10, 2),
#     ("Book", 50, 3),
#     ("Bag", 500, 1)
# ]
# Each tuple contains:
# (product, price, quantity)
# Calculate the total bill.
# Expected calculation:
# Pen  = 10 × 2
# Book = 50 × 3
# Bag  = 500 × 1
# cart = [
#     ("Pen", 10, 2),
#     ("Book", 50, 3),
#     ("Bag", 500, 1)
# ]
# total=0
#
# for i,p,q in cart:
#     total+=p*q
#
# print("Total Bill = ",total)

# ________________________________________





#
#
# Absolutely 👍 These are actual exam-style mixed coding questions, not just topic-wise questions. Here is another set at the same level, including patterns + functions + lists + strings + nested lists + lambda/map/filter/reduce.
# 🔥 Pattern Questions — Logic Based
# Q31. Increasing Number Pattern
# For n = 5, print:
# 1
# 23
# 456
# 78910
# 1112131415
# The numbers must continue increasing from the previous row.
# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=1
#     print()
# ________________________________________
# Q32. Repeated Number Pattern
# For n = 5, print:
# 1
# 22
# 333
# 4444
# 55555

#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# Condition: Use only one outer loop and string repetition.
# ________________________________________
# Q33. Reverse Number Pattern
# For n = 5, print:
# 12345
# 1234
# 123
# 12
# 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# Try solving using nested loops.
# ________________________________________
# Q34. Reverse Increasing Pattern
# For n = 5, print:
# 54321
# 4321
# 321
# 21
# 1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# ________________________________________
# Q35. Star Pyramid
# For n = 5, print:
#     *
#    ***
#   *****
#  *******
# *********
#
# for i in range(1,6):
#     for j in range(1,i+1):

# ________________________________________
# Q36. Number Pyramid
# For n = 5, print:
#     1
#    222
#   33333
#  4444444
# 555555555
# Hint: Think about spaces + repetition.
# ________________________________________
# Q37. Continuous Number Triangle
# For n = 4, print:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# The numbers should continue across rows.
# ________________________________________
# Q38. Palindrome Number Pattern
# For n = 5, print:
#     1
#    121
#   12321
#  1234321
# 123454321


   ###################################################
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end="")
#         else:
#             print(0,end="")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=1
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=2
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(1,end="")
#         else:
#             print(0,end="")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=1
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k+=2
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# for i in range(1,6):
#     print(" "*(5-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#
#     print()