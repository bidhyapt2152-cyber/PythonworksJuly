# # Q1. Most Frequent Element
# # Write a function most_frequent(lst) that accepts a list of integers and returns the element that occurs the maximum
# # number of times.
#
# # Example:
# # Input:  [4, 1, 2, 1, 2, 1, 5]
# # Output: 1
# l=[4, 1, 2, 1, 2, 1, 5]
#
# def most_frequent(lst):
#     max_count=0
#     result=None
#
#     for i in l:
#         count=l.count(i)
#
#         if count>max_count:
#             max_count=count
#             result=i
#
#     return result
# print(most_frequent(l))

# Q14. Second Most Frequent
# Write a function that returns the second most frequently occurring element in a list.
# Input:
# [1, 2, 2, 3, 3, 3, 4, 4]
#
# Output:
# 2
#
# l=[1, 2, 2, 3, 3, 3, 4, 4]
# def fun(lst):
#     max_count=0
#     second_max_count=0
#     first=None
#     second=None
#
#     for i in lst:
#         count=lst.count(i)
#
#         if count>max_count:
#             second_max_count=max_count
#             second=first
#
#
#
#             max_count=count
#             first= i
#
#
#         elif count>second_max_count and count!=max_count:
#             second_max_count=count
#
#             second=i
#
#     return second
# l=[1, 2, 2, 3, 3, 3, 4, 4]
# print(fun(l))

# # Q2. Move Zeros
# # Write a program to move all 0s in a list to the end while maintaining the order of the non-zero elements.
#
# # Input:  [0, 5, 0, 3, 4, 0, 2]
# # Output: [5, 3, 4, 2, 0, 0, 0]
# # Condition: Don't create a new list containing the non-zero elements and then add zeros. Try modifying the list
# # logically.
#
# l=[0, 5, 0, 3, 4, 0, 2]
#
# new=[]
#
# for i in l:
#     if i!=0:
#         new.append(i)
#
# for i in l:
#     if i==0:
#         new.append(i)
#
# print(new)
#
#
# # Q3. Character Frequency
# # Write a program to find the frequency of every character in a string.
#
# # Input:  "programming"
# # Output: {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}
# # Ignore spaces.
#
# s="programming"
# new={}
# for i in s:
#     new[i]=s.count(i)
# print(new)



# Q4. Vowel With Highest Frequency
# Write a program to find which vowel occurs most frequently in a given string.
# Input:  "education is important"
# Output: 'i'
# If more than one vowel has the same highest frequency, display all such vowels.
#
# s="education is important"
# max_count=0
# result=None
#
# for i in s:
#     if i in "aeiouAEIOU":
#         count=s.count(i)
#
#         if count>max_count:
#             max_count=count
#
#             result=i
# print(result)


# Q5. Second Largest Without sort()
# Write a program to find the second largest unique number in a list without using sort() or sorted().
# Input:  [10, 5, 8, 10, 3, 8]
# Output: 8

# l=[10, 5, 8, 10, 3, 8]
# largest=0
# second=0
#
#
# for i in l:
#     if i>largest:
#         largest=i
#
#     elif i>second and i!=largest:
#         second=i
#
# print(second)



# Q6. Remove Duplicate Characters
# Write a program that removes repeated characters from a string while preserving the original order.
# Input:  "programming"
# Output: "progamin"
# s="programming"
# rep=""
# for i in s:
#     if i not in rep:
#         rep+=i
#
# print(rep)

# Q7. Reverse Only Words
# Write a program that reverses each word in a sentence but keeps the order of the words unchanged.
# Input:  "hello world python"
# Output: "olleh dlrow nohtyp"

# s="hello world python"
#
# l = s.split()
#
# new = []
#
# for i in l:
#     new.append(i[::-1])
## print(new)
#
# print(" ".join(new))

# Q8. Word With Maximum Length
# Write a function that accepts a sentence and returns the longest word.
# Input:  "Python programming is interesting"
# Output: "programming"
# If multiple words have the same maximum length, return the first one.
#
# def longest(s):
#     #s="Python programming is interesting"
#     l=s.split()
#     max_len=0
#     result=None
#     for i in l:
#         if len(i)>max_len:
#             max_len=len(i)
#             result=i
#     return result
#     #print("Longest word:", result)
# s="Python programming is interesting"
# a=longest(s)
# print(a)



# Q9. Common Elements Without Duplicates
# Write a program to find the common elements between two lists.
# List 1: [1, 2, 2, 3, 4, 5]
# List 2: [2, 2, 4, 6, 7]
#
# Output: [2, 4]

# a=[1, 2, 2, 3, 4, 5]
# b=[2, 2, 4, 6, 7]
#
# new=[]
# for i in a:
#     if i in b and i not in new:
#         new.append(i)
#
# print(new)


# Q10. Separate Numbers
# Given a list containing positive, negative, and zero values, create a new list where:
# 1. Positive numbers come first
# 2. Negative numbers come next
# 3. Zeros come last
# Maintain the original order within each category.
# Input:  [0, -2, 5, -1, 0, 8, -4]
# Output: [5, 8, -2, -1, -4, 0, 0]

# l= [0, -2, 5, -1, 0, 8, -4]
#
# new=[]
#
# for i in l:
#     if i>0:
#         new.append(i)
#
# for i in l:
#     if i<0:
#         new.append(i)
#
# for i in l:
#     if i==0:
#         new.append(i)
#
# print(new)

# Q11. Count Unique Elements
# Write a program to count how many unique elements are present in a list.
# Input:  [1, 2, 2, 3, 4, 4, 5]
# Output: 5
#
# l=[1, 2, 2, 3, 4, 4, 5]
# count=0
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
#         count+=1
# print(count)


# Q12. First Non-Repeating Character
# Write a program to find the first character that appears only once in a string.
# Input:  "aabbcddee"
# Output: "c"
# If every character is repeated, print "No unique character".
# s="aabbcddee"
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break
#
# else:
#     print("No unique character")



# Q13. First Repeating Element
# Write a program to find the first element that appears more than once.
# Input:  [5, 3, 4, 3, 5, 2]
# Output: 3
# l=[5, 3, 4, 3, 5, 2]
# for i in l:
#     if l.count(i)>1:
#         print(i)
#         break


# Q14. Remove All Occurrences
# Write a program to remove all occurrences of a given number from a list.
# Input:  [1, 2, 3, 2, 4, 2, 5]
# Number: 2
#
# Output: [1, 3, 4, 5]
# l=[1, 2, 3, 2, 4, 2, 5]
# num=2
# new=[]
# for i in l:
#     if i!=num:
#         new.append(i)
# print(new)

# Q15. Move Negative Numbers to Beginning
# Move all negative numbers to the beginning while maintaining the order of both negative and non-negative numbers.
# Input:  [5, -2, 8, -1, 3, -4]
# Output: [-2, -1, -4, 5, 8, 3]
# l=[5, -2, 8, -1, 3, -4]
# new=[]
# for i in l:
#     if i<0:
#         new.append(i)
# for i in l:
#     if i>0:
#         new.append(i)
# print(new)


# Q16. Find Missing Number
# A list contains numbers from 1 to n, but one number is missing. Find the missing number.
# Input:  [1, 2, 3, 5, 6]
# Output: 4
# Condition: Don't use set().
# l=[1, 2, 3, 5, 6]
# n=6
# total=n*(n+1)//2
# m=total-sum(l)
# print("Missing Number :",m)


# Q17. Find All Duplicate Elements
# Write a program to find all elements that occur more than once.
# Input:  [1, 2, 3, 2, 4, 1, 5, 3]
# Output: [1, 2, 3]
# Each duplicate should appear only once in the output.

# l=[1, 2, 3, 2, 4, 1, 5, 3]
# new=[]
# for i in l:
#     if l.count(i)>1 and i not in new:
#
#         new.append(i)
# print(new)

# Q18. Second Smallest Unique Number
# Find the second smallest unique number without using sort() or sorted().
# Input:  [8, 3, 5, 3, 1, 8, 2]
# Output: 2
# l= [8, 3, 5, 3, 1, 8, 2]
# smallest=float("inf")
# second=float("inf")
#
# for i in l:
#     if i<smallest:
#         smallest=i
#
#     elif i<second and i!=smallest:
#         second=i
#
# print(second)




# Q19. Largest and Smallest Difference
# Find the difference between the largest and smallest elements without using max() or min().
# Input:  [10, 4, 8, 2, 15]
# Output: 13
# Because:
# 15 - 2 = 13
#
# l=[10, 4, 8, 2, 15]
# largest=float("-inf")
# smallest=float("inf")
#
# for i in l:
#     if i>largest:
#         largest=i
#
# for i in l:
#     if i<smallest:
#         smallest=i
#
# print(largest-smallest)

# Q20. Reverse a List Without reverse()
# Reverse a list without using:
# reverse()
#
# or
# [::-1]
#
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# l= [1, 2, 3, 4, 5]
# new=[]
#
# for i in range(len(l)-1,-1,-1):
#     new.append(l[i])
# print(new)


# 🔥 String Logic Questions
# Q21. Count Vowels and Consonants
# Write a program to count the number of vowels and consonants in a string.
# Ignore spaces and numbers.
# Input:  "Hello World"
# Output:
# Vowels: 3
# Consonants: 7
# s="Hello World"
# v=0
# c=0
#
# for i in s:
#     if i in 'AEIOUaeiou':
#         v+=1
#
#
#
#     elif i not in "AEIOUaeiou ":
#         c+=1
#
# print("Vowels :", v)
# print("Consonants :",c)


# Q22. Find Most Frequent Character
# Find the character that occurs the maximum number of times.
# Ignore spaces.
# Input:  "banana"
# Output: "a"
# s="banana"
# max_count=0
# result=None
#
# for i in s:
#     if s.count(i)>max_count:
#         max_count=s.count(i)
#         result=i
#
# print(result)

# Q23. Remove Duplicate Words
# Remove repeated words from a sentence while preserving the original order.
# Input:  "python is easy and python is powerful"
#
# Output:
# "python is easy and powerful"
# s="python is easy and python is powerful"
# sp=s.split()
# #print(sp)
# new=[]
# for i in sp:
#     if i not in new:
#         new.append(i)
#
#
#
# print(" ".join(new))                     #Qn 7


# Q24. Reverse a String Without Slicing
# Reverse a string without using:
# [::-1]
#
# Example:
# Input:  "python"
# Output: "nohtyp"
# s="python"
# rev=""
#
# for i in s:
#     rev=i+rev
# print(rev)

# Q25. Check Palindrome
# Write a function to check whether a string is a palindrome.
# Input:  "madam"
# Output: True
# Input:  "python"
# Output: False
# Condition: Don't use slicing.
# s="python"
#
#
# if s==s[::-1]:
#     print("True")
#
# else:
#     print("False")




# Q26. Longest Word Length
# Find the length of the longest word in a sentence.
# Input:  "Python programming language"
# Output: 11

# s="Python programming language"
# sp=s.split()
# longest=0
# for i in sp:
#     length=len(i)
#     if length>longest:
#         longest=length
#
# print(longest)

# Q27. Word Frequency
# Count how many times each word occurs in a sentence.
# Input:
# "python is easy python is powerful"
#
# Output:
# python : 2
# is : 2
# easy : 1
# powerful : 1
# s = "python is easy python is powerful"
# sp=s.split()
# new=[]
#
# for i in sp:
#     if i not in new:
#         new.append(i)
#
#         print(i,":",sp.count(i))


# Q28. Character With Second Highest Frequency
# Find the character having the second-highest frequency.
# Input:  "aabbcccdd"
#
# Output: "a"
# Here:
# c → 3
# a → 2
# b → 2
# d → 2

# s="aaabbccccdd"                                     #Qn 12, Qn 14
#
# max_count=0
# second_count=0
# first=None
# second=None
#
# for i in s:
#     count=s.count(i)
#     if count>max_count:
#         second_count=max_count
#         second=first
#
#         max_count=count
#         first=i
#
#     elif count>second_count and count!=max_count:
#         second_count=count
#         second=i
#
# print(second)



# If there is a tie, return the first character according to its appearance.
# 🔥 Number Logic Questions
# Q29. Separate Even and Odd
# Create a new list where even numbers come first and odd numbers come next.
# Maintain their original order.
# Input:  [5, 2, 8, 3, 1, 6, 4]
#
# Output: [2, 8, 6, 4, 5, 3, 1]

# l=[5, 2, 8, 3, 1, 6, 4]
# new=[]
# for i in l:
#     if i%2==0:
#         new.append(i)
#
# for i in l:
#     if i%2!=0:
#         new.append(i)
#
# print(new)

# Q30. Sum of Digits
# Write a function to find the sum of digits of a number.
# Input:  5832
# Output: 18
# Because:
# 5 + 8 + 3 + 2 = 18

# num=5832
#
# th=num//1000
# h=(num//100)%10
# t=(num//10)%10
# o=num%10
#
# print(th+h+t+o)

# Q31. Reverse a Number
# Reverse a number without converting it into a string.
# Input: 12345
# Output: 54321

# num=12345
#
# a=num//10000
# b=(num//1000)%10
# c=(num//100)%10
# d=(num//10)%10
# e=num%10
#
# print((e*10000)+(d*1000)+(c*100)+(b*10)+a)


# Q32. Count Digits
# Count the number of digits in an integer without converting it into a string.
# Input: 58392
# Output: 5

# num=58392
# count=0
#
# while num>0:
#     count+=1
#     num=num//10
#
# print(count)



# Q33. Find Second Most Frequent Number
# Find the number having the second-highest frequency.
# Input: [1, 2, 2, 3, 3, 3, 4, 4]
#
# Output: 2

# l=[1, 2,2, 3, 3, 3, 4, 4]
# count_max=0
# count_second=0
# first=None
# second=None
#
# for i in l:
#     count=l.count(i)
#
#     if count>count_max:
#         count_second=count_max
#         count_max=count
#
#         second=first
#         first=i
#
#     elif count>count_second and count!=count_max:
#         count_second=count
#         second=i
#
# print(second)



# Q34. Numbers Appearing Only Once
# Find all numbers that occur exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5]
#
# Output: [1, 3, 5]
#l=[1, 2, 2, 3, 4, 4, 5]

#
# count=0
#
# new=[]
# for i in l:
#     if l.count(i)==1:
#         new.append(i)
# print(new)

# Q35. Consecutive Numbers
# Find the length of the longest consecutive sequence.
# Input: [100, 4, 200, 1, 3, 2]
#
# Output: 4
# Because:
# 1, 2, 3, 4

# l=[100, 4, 200, 1, 3, 2]
#
# s=set(l)
# maximum=0
#
# for i in s:
#     if i-1 not in s:   #to find the 1st consecutive number
#         count=1
#         current=i
#
#         while current+1 in s:
#             current+=1
#             count+=1
#
#         if count>maximum:
#             maximum=count
#
# print(maximum)


# 🔥 Function-Based Questions
# Q36. Count Even and Odd
# Write a function:
# count_even_odd(lst)
#
# that returns the number of even and odd numbers.
# Input: [1, 2, 3, 4, 5, 6]
#
# Output:
# Even: 3
# Odd: 3

# def count_even_odd(lst):
#     even_count = 0
#     odd_count=0
#     for i in lst:
#
#         if i%2==0:
#             even_count+=1
#
#     for i in lst:
#         if i%2!=0:
#             odd_count+=1
#
#     print("Even :",even_count)
#     print("Odd :",odd_count)
#     return
#
#
# l=[1, 2, 3, 4, 5, 6]
# count_even_odd(l)


# Q37. Find All Numbers Greater Than Average
# Write a function that returns all numbers greater than the average of the list.
# Input: [10, 20, 30, 40, 50]
#
# Average: 30
#
# Output: [40, 50]
# l=[10, 20, 30, 40, 50]
#
#
# def greater(lst):
#     sum=0
#     count=0
#
#     for i in lst:
#         sum+=i
#         count+=1
#
#     avg=sum/count
#
#     average=int(avg)
#
#     new=[]
#     for i in lst:
#         if i>average:
#             new.append(i)
#     print(new)
#
#
#     return
# l=[10, 20, 30, 40, 50]
# greater(l)

# Q13. Rotate a List
# Write a function that takes a list and a number k and moves the last k elements to the beginning.
# Input:
# [1, 2, 3, 4, 5]
# k = 2
#
# Output:
# [4, 5, 1, 2, 3]
# l=[1, 2, 3, 4, 5]
#
# k=2
#
# k=k%len(l)     #since k=2 which is less than 5 therefore, k is 2 itself, suppose k=7  after this step k becomes 2
#                # ie, 2%5 is same as 7%5
# result=l[-k:]+l[:-k]
# print(result)


# Q38. Rotate List
# Rotate a list to the right by k positions.
# Input: [1, 2, 3, 4, 5]
# k = 2
#
# Output: [4, 5, 1, 2, 3]

# l=[1, 2, 3, 4, 5]
# k=2
# k=k%len(l)
# print(l[-k:]+l[:-k])

# Q39. Common Elements in Three Lists
# Find elements common to all three lists without duplicates.
# List 1: [1, 2, 3, 4, 5]
# List 2: [2, 3, 4, 6]
# List 3: [3, 4, 7]
#
# Output: [3, 4]

# l1=[1, 2, 3, 4, 5]
# l2=[2, 3, 4, 6]
# l3=[3, 4, 7]
#
# new=[]
# for i in l3:
#     if i in l2 and i in l1:
#         new.append(i)
# print(new)

# Q40. Frequency of Each Number
# Write a function that returns the frequency of every number.
# Input: [2, 3, 2, 4, 3, 2]
#
# Output:
# 2 : 3
# 3 : 2
# 4 : 1

# def frequency(lst):
#     new=[]
#     for i in lst:
#         if i not in new:
#             new.append(i)
#
#             print(i,":",lst.count(i))
#
#     return
# l=[2, 3, 2, 4, 3, 2]
# frequency(l)


# 🧠 Slightly Harder Exam-Level Questions

# Q41. Remove All Duplicates
# Unlike Q6, here keep only elements that occur exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5]
#
# Output: [1, 3, 5]
# l=[1, 2, 2, 3, 4, 4, 5]
# new=[]
#
# for i in  l:
#     if i not in new and l.count(i)==1:
#         new.append(i)
# print(new)

# Q42. Maximum Difference Between Two Elements
# Find the maximum possible difference between two elements without using max() or min().
# Input: [7, 1, 5, 3, 6]
#
# Output: 6
# l=[7, 1, 5, 3, 6]
# larger=0
# smaller=float("inf")          #Qn 18
# for i in l:
#     if i>larger:
#         larger=i
#
#     elif i<smaller:
#         smaller=i
#
# for i in l:
#     difference=larger-smaller
#
# print(difference)


# Q43. Rearrange Positive and Negative
# Rearrange the list so that positive and negative numbers appear alternately as much as possible.
# Input: [1, -2, 3, -4, 5, -6]
#
# # Output: [1, -2, 3, -4, 5, -6]
#
# l=[1,3,5,-2,-4,-6]
# p=[]
# n=[]
#
# for i in l:
#     if i>=0:
#         p.append(i)
#     else:
#         n.append(i)
# # #
# new=[]
# i=0
#
# while i<len(p) and i<len(n):
#     new.append(p[i])
#     new.append(n[i])
#
#     i+=1
#
# while i<len(p):
#     new.append(p[i])
#
#     i+=1
#
# while i < len(n):
#     new.append(n[i])
#
#     i += 1
# print(new)

# Q44. Find Leaders
# An element is called a leader if all elements to its right are smaller than it.
# Input: [16, 17, 4, 3, 5, 2]
#
# Output: [17, 5, 2]

# l=[16, 17, 4, 3, 5, 2]
# new=[]
# for i in range(len(l)):
#     leader=True
#
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             leader=False
#             break
#     if leader:
#         new.append(l[i])
#
# print(new)



# 42. Reverse a Three-Digit Number
# Take:
# 123
# and produce:
# 321

# num=123
# h=num//100
# t=(num//10)%10
# o=num%10

# print((o*100)+(t*10)+h)

# 43. Last Digit
# Take any integer and find its last digit.
# Hint: %.

# num=123
# last=num%10
# print(last)


#Q5. Multiplication Table
# Take a number from the user and print its table from 1 to 10.

# n=5
# for i in range(1,11):
#     print(f'{i} x {n} = {i*n}')


# Q10. Factorial
# Take a number:
# 5
# Calculate:
# 5 × 4 × 3 × 2 × 1 = 120

# n=5
# p=1
# for i in range(1,n+1):
#     p*=i
# print(p)

# Q9. Reverse a Number
# Take:
# 12345
# Produce:
# 54321
# Try using a while loop.
# num=12345
# rev=""
# for i in str(num):
#     rev=i+rev
#
# print(rev)



# num=12345
# rev=0
# while num>0:
#     last_digit=num%10
#     rev=rev*10+last_digit
#     num=num//10
#
# print(rev)




#Q10. Armstrong number
# num=151
# s=str(num)
# power=len(s)
#
# power_sum=0
#
# for i in s:
#     power_sum+=int(i)**power
#
#
# if num==power_sum:
#     print(f"{num}, is Armstrong")
# else:
#     print(f"{num}, is Not Armstrong")

n=5

current=0





