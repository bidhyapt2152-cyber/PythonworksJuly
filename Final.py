# QUESTIONS FOR CORE
# Q35. Consecutive Numbers
# Find the length of the longest consecutive sequence.
# Input: [100, 4, 200, 1, 3, 2]
#
# Output: 4
# Because:
# 1, 2, 3, 4

# Q32. Count Digits
# Count the number of digits in an integer without converting it into a string.
# Input: 58392
# Output: 5

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
# If there is a tie, return the first character according to its appearance.

## Q20. Reverse a List Without reverse()
# Reverse a list without using:
# reverse()
# or
# [::-1]
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# ________________________________________
# Q3. Character Frequency
# Write a program to find the frequency of every character in a string.
# Input:  "programming"
# Output: {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}
# Ignore spaces.



# ________________________________________
# Q4. Vowel With Highest Frequency
# Write a program to find which vowel occurs most frequently in a given string.
# Input:  "education is important"
# Output: 'i'
# If more than one vowel has the same highest frequency, display all such vowels.

# Q6. Remove Duplicate Characters
# Write a program that removes repeated characters from a string while preserving the original order.
# Input:  "programming"
# Output: "progamin"
# s="programming"
# lst=list(s)
# new=[]
# for i in lst:
#     if i not in new:
#         new.append(i)
# print("".join(new))

# ________________________________________
# Q7. Reverse Only Words
# Write a program that reverses each word in a sentence but keeps the order of the words unchanged.
# Input:  "hello world python"
# Output: "olleh dlrow nohtyp"


# Q1. Most Frequent Element
# Write a function most_frequent(lst) that accepts a list of integers and returns the element that occurs the maximum
# number of times.
# Example:
# Input:  [4, 1, 2, 1, 1, 4, 5]
# Output: 1
def most_frequent(lst):
    result=0
    max_count=0
    for i in lst:
        count=lst.count(i)
        if count>max_count:
            max_count=count
            result=i
    return result

l=[4, 1, 2, 1, 2, 1, 5]
a=most_frequent(l)
print(a)




# ________________________________________
# Q2. Move Zeros
# Write a program to move all 0s in a list to the end while maintaining the order of the non-zero elements.
# Input:  [0, 5, 0, 3, 4, 0, 2]
# Output: [5, 3, 4, 2, 0, 0, 0]
# Condition: Don't create a new list containing the non-zero elements and then add zeros. Try modifying the list
#  logically.

lst=[0, 5, 0, 3, 4, 0, 2]
new=[]

for i in lst:
    if i!=0:
        new.append(i)

for i in lst:
    if i==0:
        new.append(i)
print(new)




# ________________________________________
# Q5. Second Largest Without sort()
# Write a program to find the second largest unique number in a list without using sort() or sorted().
# Input:  [10, 5, 8, 10, 3, 8]
# Output: 8
l=[10, 5, 8, 10, 3, 8]
first=0
second=0

for i in l:
    if i>first:
        first=i
    elif i>second and i!=first:
        second=i

print(second)

# ________________________________________






# ________________________________________
# Q8. Word With Maximum Length
# Write a function that accepts a sentence and returns the longest word.
# Input:  "Python programming is interesting"
# Output: "programming"
# If multiple words have the same maximum length, return the first one.
s="Python programming is interesting"

def longest(word):
    sp=word.split()
    max_length=0
    result=None
    for i in sp:
        length=len(i)
        if length>max_length:
           max_length=length
           result=i
    print(result)

    return result
s="Python programming is interesting"
longest(s)

# ________________________________________
# Q9. Common Elements Without Duplicates
# Write a program to find the common elements between two lists.
# List 1: [1, 2, 2, 3, 4, 5]
# List 2: [2, 2, 4, 6, 7]
#
# Output: [2, 4]

l1=[1, 2, 2, 3, 4, 5]
l2=[2, 2, 4, 6, 7]
new=[]
for i in l2:
    if i in l1 and i not in new:
        new.append(i)
print(new)
# ________________________________________
# Q10. Separate Numbers
# Given a list containing positive, negative, and zero values, create a new list where:
# 1.	Positive numbers come first
# 2.	Negative numbers come next
# 3.	Zeros come last
# Maintain the original order within each category.
# Input:  [0, -2, 5, -1, 0, 8, -4]
# Output: [5, 8, -2, -1, -4, 0, 0]
l= [0, -2, 5, -1, 0, 8, -4]
new=[]
for i in l:
    if i>0:
        new.append(i)
for i in l:
    if i<0:
        new.append(i)
for i in l:
    if i==0:

        new.append(i)
print(new)
#
# Q11. Count Unique Elements
# Write a program to count how many unique elements are present in a list.
# Input:  [1, 2, 2, 3, 4, 4, 5]
# Output: 5
l=[1, 2, 2, 3, 4, 4, 5]
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(len(new))



# ________________________________________
# Q12. First Non-Repeating Character
# Write a program to find the first character that appears only once in a string.
# Input:  "aabbcddee"
# Output: "c"
# If every character is repeated, print "No unique character".
s="aabbcddee"
for i in s:
    if s.count(i)==1:
        print(i)
# ________________________________________
# Q13. First Repeating Element
# Write a program to find the first element that appears more than once.
# Input:  [5, 3, 4, 3, 5, 2]
# Output: 5
l=[5, 3, 4, 3, 5, 2]
for i in l:
    if l.count(i)>0:
        print(i)
        break

# ________________________________________
# Q14. Remove All Occurrences
# Write a program to remove all occurrences of a given number from a list.
# Input:  [1, 2, 3, 2, 4, 2, 5]
# Number: 2
#
# Output: [1, 3, 4, 5]
l=[1, 2, 3, 2, 4, 2, 5]
number=2
new=[]
for i in l:
    if i!=2:
        new.append(i)
print(new)

# ________________________________________
# Q15. Move Negative Numbers to Beginning
# Move all negative numbers to the beginning while maintaining the order of both negative and non-negative numbers.
# Input:  [5, -2, 8, -1, 3, -4]
# Output: [-2, -1, -4, 5, 8, 3]
l=[5, -2, 8, -1, 3, -4]
new=[]
for i in l:
    if i<0:
        new.append(i)

for i in l:
    if i>=0:
        new.append(i)
print(new)
# ________________________________________
# Q16. Find Missing Number
# A list contains numbers from 1 to n, but one number is missing. Find the missing number.
# Input:  [1, 2, 3, 5, 6]
# Output: 4
# Condition: Don't use set().
l=[1, 2, 3, 5, 6]
n=6
sn=n*(n+1)/2
s=0
for i in l:
    s+=i

print(int(sn-s))


# ________________________________________
# Q17. Find All Duplicate Elements
# Write a program to find all elements that occur more than once.
# Input:  [1, 2, 3, 2, 4, 1, 5, 3]
# Output: [1, 2, 3]
# Each duplicate should appear only once in the output.

l=[1, 2, 3, 2, 4, 1, 5, 3]
new=[]
for i in l :
    if l.count(i)>1 and i not in new:
        new.append(i)
print(new)
# ________________________________________
# Q18. Second Smallest Unique Number
# Find the second smallest unique number without using sort() or sorted().
# Input:  [8, 3, 5, 3, 1, 8, 2]
# Output: 2
l=[8, 3, 5, 3, 1, 8, 2]
first=float("inf")
second=float("inf")

for i in l:
    if i<first:
        first=i

    elif i<second and i!=first:
        second=i

print(second)




# ________________________________________
# Q19. Largest and Smallest Difference
# Find the difference between the largest and smallest elements without using max() or min().
# Input:  [10, 4, 8, 2, 15]
# Output: 13
# Because:
# 15 - 2 = 13

l= [10, 4, 8, 2, 15]
largest=0
smallest=float("inf")

for i in l:
    if i>largest:
        largest=i
    elif i<smallest:
        smallest=i

print(largest-smallest)



# ________________________________________





# ________________________________________
# 🔥 String Logic Questions
# Q21. Count Vowels and Consonants
# Write a program to count the number of vowels and consonants in a string.
# Ignore spaces and numbers.
# Input:  "Hello World"
# Output:
# Vowels: 3
# Consonants: 7

s="Hello World"
v=0
c=0
for i in s:
    if i in "aeiouAEIOU":
        v+=1


    elif i not in "AEIOUaeiou ":
        c+=1
print("Vowels: ", v)
print("Consonants: ",c)

# ________________________________________
# Q22. Find Most Frequent Character
# Find the character that occurs the maximum number of times.
# Ignore spaces.
# Input:  "banana"
# Output: "a"

s="banana"
max_count=0
result=None

for i in s:
    count=s.count(i)
    if count>max_count:
        max_count=count
        result=i
print(result)

# ________________________________________
# Q23. Remove Duplicate Words
# Remove repeated words from a sentence while preserving the original order.
# Input:  "python is easy and python is powerful"
#
# Output:
# "python is easy and powerful"
s="python is easy and python is powerful"
sp=s.split()
new=[]
for i in sp:
    if i not in new:
        new.append(i)

print(" ".join(new))



# ________________________________________
# Q24. Reverse a String Without Slicing
# Reverse a string without using:
# [::-1]
# Example:
# Input:  "python"
# Output: "nohtyp"

s="python"
rev=""
for i in s:
    rev=i+rev
print(rev)
# ________________________________________
# Q25. Check Palindrome
# Write a function to check whether a string is a palindrome.
# Input:  "madam"
# Output: True
# Input:  "python"
# Output: False
# Condition: Don't use slicing.


def palindrome(s):
    for i in s:
        if s==s[::-1]:
            print("True")
            break
        else:
            print("False")
            break
    return

st="madam"
py="Python"
palindrome(py)

# ________________________________________
# Q26. Longest Word Length
# Find the length of the longest word in a sentence.
# Input:  "Python programming language"
# Output: 11
s="Python programming language"
sp=s.split()
max_length=0
result=None
for i in sp:
    length=len(i)
    if length>max_length:
        max_length=length
        result=i
print(len(result))


# ________________________________________
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
s="python is easy python is powerful"
sp=s.split()

new=[]
for i in sp:
    if i not in new:
        new.append(i)
        print(i ,":",sp.count(i))

# ________________________________________


# ________________________________________
# 🔥 Number Logic Questions
# Q29. Separate Even and Odd
# Create a new list where even numbers come first and odd numbers come next.
# Maintain their original order.
# Input:  [5, 2, 8, 3, 1, 6, 4]
#
# Output: [2, 8, 6, 4, 5, 3, 1]

l=[5, 2, 8, 3, 1, 6, 4]
new=[]
for i in l:
    if i%2==0:
        new.append(i)

for i in l:
    if i%2!=0:
        new.append(i)

print(new)

# ________________________________________
# Q30. Sum of Digits
# Write a function to find the sum of digits of a number.
# Input:  5832
# Output: 18
# Because:
# 5 + 8 + 3 + 2 = 18

def add(num):
    t=num//1000
    h=(num//100)%10
    tens=(num//10)%10
    o=num%10

    s=t+h+tens+o

    print(s)
    return
n=5832
add(n)

# ________________________________________
# Q31. Reverse a Number
# Reverse a number without converting it into a string.
# Input: 12345
# Output: 54321

num=12345

a=num//10000
b=(num//1000)%10
c=(num//100)%10
d=(num//10)%10
e=num%10

print((e*10000)+(d*1000)+(c*100)+(b*10)+a)

# ________________________________________




# ________________________________________
# Q33. Find Second Most Frequent Number
# Find the number having the second-highest frequency.
# Input: [1, 2, 2, 3, 3, 3, 4, 4]
#
# Output: 2

l= [1, 2, 2, 3, 3, 3, 4, 4]
max_count=0
second_max=0
first=None
second=None

for i in l:
   count=l.count(i)
   if count>max_count:
       second_max=max_count
       max_count=count

       second=first
       first=i

   elif count>second_max and count!=max_count:
       second_max=count
       second=i
print(second)

# ________________________________________
# Q34. Numbers Appearing Only Once
# Find all numbers that occur exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5]
#
# Output: [1, 3, 5]

l=[1, 2, 2, 3, 4, 4, 5]
new=[]
for i in l:
    if l.count(i)==1 and i not in new:
        new.append(i)
print(new)
# ________________________________________



# ________________________________________
# 🔥 Function-Based Questions
# Q36. Count Even and Odd
# Write a function:
# count_even_odd(lst)
# that returns the number of even and odd numbers.
# Input: [1, 2, 3, 4, 5, 6]
#
# Output:
# Even: 3
# Odd: 3
# ________________________________________
# Q37. Find All Numbers Greater Than Average
# Write a function that returns all numbers greater than the average of the list.
# Input: [10, 20, 30, 40, 50]
#
# Average: 30
#
# Output: [40, 50]
# ________________________________________
# Q38. Rotate List
# Rotate a list to the right by k positions.
# Input: [1, 2, 3, 4, 5]
# k = 2
#
# Output: [4, 5, 1, 2, 3]

l=[1, 2, 3, 4, 5]
k=2

k=k%len(l)
print(l[-k:]+l[:-k])
# ________________________________________
# Q39. Common Elements in Three Lists
# Find elements common to all three lists without duplicates.
# List 1: [1, 2, 3, 4, 5]
# List 2: [2, 3, 4, 6]
# List 3: [3, 4, 7]
#
# Output: [3, 4]
# ________________________________________
# Q40. Frequency of Each Number
# Write a function that returns the frequency of every number.
# Input: [2, 3, 2, 4, 3, 2]
#
# Output:
# 2 : 3
# 3 : 2
# 4 : 1
l=[2, 3, 2, 4, 3, 2]
new=[]
for i in l:
    if i not in new:
        new.append(i)

        print(i,":",l.count(i))


# ________________________________________
# 🧠 Slightly Harder Exam-Level Questions
# These are especially good for your retest because you'll have to decide the logic yourself.
# Q41. Remove All Duplicates
# Unlike Q6, here keep only elements that occur exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5]
#
# Output: [1, 3, 5]
# ________________________________________
# Q42. Maximum Difference Between Two Elements
# Find the maximum possible difference between two elements without using max() or min().
# Input: [7, 1, 5, 3, 6]
#
# Output: 6
# ________________________________________
# Q43. Rearrange Positive and Negative
# Rearrange the list so that positive and negative numbers appear alternately as much as possible.
# Input: [1, -2, 3, -4, 5, -6]
#
# Output: [1, -2, 3, -4, 5, -6]
# ________________________________________
# Q44. Find Leaders
# An element is called a leader if all elements to its right are smaller than it.
# Input: [16, 17, 4, 3, 5, 2]
#
# Output: [17, 5, 2]
# ________________________________________
# Q45. Longest Increasing Consecutive Part
# Find the length of the longest continuously increasing portion of a list.
# Input: [1, 2, 3, 2, 4, 5, 6, 1]
#
# Output: 3
# Because:
# 4, 5, 6
# is the longest increasing consecutive part
#
# ________________________________________
# ________________________________________
#
# SET 2
#
#
#
#
#
#
#
#
#
#
# 🔥 Function-Based Questions
# Q11. Numbers Appearing Once
# Define a function that accepts a list and returns all elements that occur exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5, 6, 6]
#
# Output: [1, 3, 5]
# ________________________________________
# Q12. Find Missing Number
# A list contains numbers from 1 to n, but one number is missing.
# Write a function to find the missing number.
# Input:  [1, 2, 3, 5, 6]
# Output: 4
# ________________________________________
# Q13. Rotate a List
# Write a function that takes a list and a number k and moves the last k elements to the beginning.
# Input:
# [1, 2, 3, 4, 5]
# k = 2
#
# Output:
# [4, 5, 1, 2, 3]
# ________________________________________
# Q14. Second Most Frequent
# Write a function that returns the second most frequently occurring element in a list.
# Input:
# [1, 2, 2, 3, 3, 3, 4, 4]
#
# Output:
# 2
#
# Q15. First Non-Repeating Element
# Define a function that accepts a list and returns the first element that occurs exactly once.
# Input:
# [4, 2, 5, 2, 4, 6, 5, 7]
# Output:
# 6
# ________________________________________
# Q16. Find Duplicate Elements
# Define a function that accepts a list and returns all elements that occur more than once.
# Input:
# [1, 2, 3, 2, 4, 1, 5, 3]
# Output:
# [1, 2, 3]
# Each element should appear only once in the output.
# ________________________________________
# Q17. Second Smallest Unique Element
# Define a function that accepts a list and returns the second smallest unique element.
# Condition: Don't use sort() or sorted().
# Input:
# [8, 3, 5, 3, 1, 8, 2]
# Output:
# 2
# ________________________________________
# Q18. Move Zeros to End
# Define a function that moves all zeros to the end while maintaining the order of the other elements.
# Input:
# [0, 4, 0, 2, 5, 0, 3]
# Output:
# [4, 2, 5, 3, 0, 0, 0]
# ________________________________________
# Q19. Separate Even and Odd
# Define a function that returns a list where all even numbers come first and odd numbers come next.
# Maintain the original order.
# Input:
# [5, 2, 8, 3, 1, 6, 4]
# Output:
# [2, 8, 6, 4, 5, 3, 1]
# ________________________________________
# Q20. Find Common Elements
# Define a function that accepts two lists and returns their common elements without duplicates.
# Input:
# list1 = [1, 2, 2, 3, 4, 5]
# list2 = [2, 2, 4, 6, 7]
# Output:
# [2, 4]
# ________________________________________
# Q21. Most Frequent Element
# Define a function that returns the element occurring the maximum number of times.
# Input:
# [4, 1, 2, 1, 2, 1, 5]
# Output:
# 1
# ________________________________________
# Q22. Second Largest Unique Element
# Define a function that returns the second largest unique number.
# Condition: Don't use sort() or sorted().
# Input:
# [10, 5, 8, 10, 3, 8]
# Output:
# 8
# ________________________________________
# Q23. Remove Duplicates
# Define a function that removes duplicate elements while preserving their original order.
# Input:
# [4, 2, 4, 1, 2, 5, 1]
# Output:
# [4, 2, 1, 5]
# ________________________________________
# Q24. Find Elements Greater Than Average
# Define a function that returns all elements greater than the average of the list.
# Input:
# [10, 20, 30, 40, 50]
# Output:
# [40, 50]
# ________________________________________
# Q25. Count Even, Odd and Zero
# Define a function that accepts a list and returns the count of even numbers, odd numbers, and zeros.
# Input:
# [2, 5, 0, 8, 7, 0, 4]
# Output:
# Even: 3
# Odd: 2
# Zero: 2
# ________________________________________
# Q26. Reverse List
# Define a function that reverses a list.
# Condition: Don't use reverse() or slicing.
# Input:
# [1, 2, 3, 4, 5]
# Output:
# [5, 4, 3, 2, 1]
# ________________________________________
# Q27. Find Missing Number
# Define a function that finds the missing number from a list containing numbers from 1 to n.
# Input:
# [1, 2, 3, 4, 6, 7, 8]
# Output:
# 5
# ________________________________________
# Q28. Rotate List Left
# Define a function that moves the first k elements to the end.
# Input:
# [1, 2, 3, 4, 5]
# k = 2
# Output:
# [3, 4, 5, 1, 2]
# ________________________________________
# Q29. Find First Repeating Element
# Define a function that returns the first element that appears more than once.
# Input:
# [5, 3, 4, 3, 5, 2]
# Output:
# 5
# ________________________________________
# Q30. Sum of Unique Elements
# Define a function that returns the sum of elements that occur exactly once.
# Input:
# [1, 2, 2, 3, 4, 4, 5]
# Unique elements are:
# 1, 3, 5
# Output:
# 9
# ________________________________________
# 🔥 Slightly Harder
# Q31. Second Most Frequent Unique Element
# Define a function that returns the element with the second-highest frequency.
# Input:
# [1, 2, 2, 3, 3, 3, 4, 4]
# Output:
# 2
# ________________________________________
# Q32. Find Leaders in a List
# An element is called a leader if every element to its right is smaller than it.
# Define a function to return all leaders.
# Input:
# [16, 17, 4, 3, 5, 2]
# Output:
# [17, 5, 2]
# ________________________________________
# Q33. Separate Positive, Negative and Zero
# Define a function that returns:
# 1.	Positive numbers first
# 2.	Negative numbers next
# 3.	Zeros last
# Maintain the original order within each group.
# Input:
# [0, -2, 5, -1, 0, 8, -4]
# Output:
# [5, 8, -2, -1, -4, 0, 0]
# ________________________________________
# Q34. Longest Word
# Define a function that accepts a sentence and returns the longest word.
# If multiple words have the same length, return the first one.
# Input:
# "Python programming is interesting"
# Output:
# "programming"
# ________________________________________
# Q35. Character With Highest Frequency
# Define a function that accepts a string and returns the character that occurs most frequently.
# Ignore spaces.
# Input:
# "banana"
# Output:
# "a"
# ________________________________________
# Q36. Filter Numbers
# Define a function that accepts a list and returns only numbers that are:
# •	even
# •	greater than 10
# Input:
# [5, 12, 7, 18, 20, 9, 4, 15]
# Output:
# [12, 18, 20]
# ________________________________________
# Q37. Square Even Numbers
# Define a function that accepts a list and returns the squares of only the even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [4, 16, 36]
# 💡 This one can be solved using filter() + map().
# ________________________________________
# Q38. Product of All Elements
# Define a function that returns the product of all elements in a list.
# Input:
# [2, 3, 4, 5]
# Output:
# 120
# 💡 Try this using reduce().
# ________________________________________
# Q39. Find Largest Using reduce()
# Define a function that finds the largest element using reduce().
# Input:
# [12, 45, 7, 23, 56, 18]
# Output:
# 56
# ________________________________________
# Q40. Filter Names
# Define a function that returns names that:
# •	start with "A"
# •	have more than 4 characters
# Input:
# ["Anu", "Anjali", "Arjun", "Akhil", "Binu", "Amal"]
# Output:
# ["Anjali", "Arjun", "Akhil"]
#
#
#
#
#
# SET 3
#
# 🔥 Lambda / Higher Order Function Questions
# Q15. Filter and Transform
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter() and map(), produce the squares of only the even numbers.
# Expected:
# [4, 16, 36, 64, 100]
# ________________________________________
# Q16. Filter Names
# Given:
# names = ["Arun", "Anu", "Rahul", "Amal", "Riya", "Akhil"]
# Using filter() and lambda, return names that:
# •	start with "A"
# •	and have more than 4 characters.
# Expected:
# ["Arun", "Amal", "Akhil"]
# ________________________________________
# Q17. Reduce — Largest Number
# Using reduce() and lambda, find the largest number from:
# numbers = [12, 45, 7, 89, 34, 23]
# Expected:
# 89
# ________________________________________
# Q18. Reduce — Product
# Using reduce() and lambda, calculate the product of all numbers in a list.
# Input: [2, 3, 4, 5]
# Output: 120
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
# But without using nested loops.
# ________________________________________
# Q22.
# For n = 5:
# 1
# 22
# 333
# 4444
# 55555
# Try solving using a single outer loop and string repetition.
# ________________________________________
# Q23.
# Print:
# 1
# 23
# 456
# 78910
# For n = 4.
# The numbers should continue increasing rather than restarting from 1 on every row.
# ________________________________________
# Q24.
# For n = 5:
#     1
#    121
#   12321
#  1234321
# 123454321
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
# ________________________________________
# Q27. Password Validation
# Write a function that accepts a password and returns True only if:
# •	length ≥ 8
# •	contains at least one digit
# •	contains at least one uppercase letter
# •	contains at least one lowercase letter
# Otherwise return False.
# ________________________________________
# Q28. Sentence Analysis
# Write a function that accepts a sentence and returns:
# Number of words
# Number of vowels
# Number of consonants
# Longest word
# Most frequent character
# Ignore spaces while counting characters.
# ________________________________________
# Q29. Nested List
# Given:
# numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Write a program to find:
# Total number of elements
# Sum of all elements
# Largest element
# without using sum() or max().
# ________________________________________
# Q30. Mini Challenge ⭐
# Write a function that accepts a list of integers and returns a dictionary containing:
# even   → number of even elements
# odd    → number of odd elements
# zero   → number of zeros
# Example:
# Input:
# [2, 0, 5, 8, 0, 3, 7, 4]
#
# Output:
# {
#     "even": 3,
#     "odd": 3,
#     "zero": 2
# }
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
# ________________________________________
# Q32. Repeated Number Pattern
# For n = 5, print:
# 1
# 22
# 333
# 4444
# 55555
# Condition: Use only one outer loop and string repetition.
# ________________________________________
# Q33. Reverse Number Pattern
# For n = 5, print:
# 12345
# 1234
# 123
# 12
# 1
# Try solving using nested loops.
# ________________________________________
# Q34. Reverse Increasing Pattern
# For n = 5, print:
# 54321
# 4321
# 321
# 21
# 1
# ________________________________________
# Q35. Star Pyramid
# For n = 5, print:
#     *
#    ***
#   *****
#  *******
# *********
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
# ________________________________________
# 🧩 Mixed Function Questions
# Q39. Student Result
# Write a function:
# student_result(marks)
# that returns:
# •	highest mark
# •	lowest mark
# •	average
# •	number of passed students
# •	number of failed students
# Passing mark = 40.
# Input:
# [35, 78, 45, 90, 22, 56]
# Expected:
# Highest: 90
# Lowest: 22
# Average: ...
# Passed: 4
# Failed: 2
# ________________________________________
# Q40. Employee Salary Analysis
# Given:
# employees = [
#     ("Anu", 25000),
#     ("Arun", 35000),
#     ("Meera", 28000),
#     ("Rahul", 45000)
# ]
# Write a function that finds:
# 1.	Highest salary
# 2.	Lowest salary
# 3.	Average salary
# 4.	Number of employees earning more than 30000
# ________________________________________
# Q41. Shopping Cart With Discount
# Given:
# cart = [
#     ("Pen", 10, 2),
#     ("Book", 50, 3),
#     ("Bag", 500, 1)
# ]
# Calculate:
# •	Total before discount
# •	Discount = 10% if total is greater than 500
# •	Final bill
# Expected format:
# Total: ...
# Discount: ...
# Final Bill: ...
# ________________________________________
# Q42. Number Analysis Function
# Write:
# analyze_numbers(lst)
# It should return:
# •	largest
# •	smallest
# •	total
# •	average
# •	even count
# •	odd count
# Input:
# [10, 5, 8, 3, 12, 7]
# ________________________________________
# Q43. Password Validation
# Write a function:
# validate_password(password)
# Return True only if:
# •	length ≥ 8
# •	contains digit
# •	contains uppercase
# •	contains lowercase
# •	contains special character
# Example:
# Input: "Python@123"
# Output: True
# Input: "python123"
# Output: False
# ________________________________________
# 🔥 String Logic
# Q44. Sentence Analyzer
# Write a function:
# analyze_sentence(sentence)
# Return:
# •	number of words
# •	number of vowels
# •	number of consonants
# •	longest word
# Input:
# "Python is very interesting"
# ________________________________________
# Q45. Character Frequency Analyzer
# Write a function that returns the frequency of every character.
# Ignore spaces and treat uppercase/lowercase as the same.
# Input:
# "Hello World"
# Expected concept:
# h → 1
# e → 1
# l → 3
# o → 2
# ...
# ________________________________________
# Q46. Most Frequent Word
# Write a function that finds the most frequently occurring word in a sentence.
# Input:
# "python is easy and python is powerful"
# Output:
# python
# ________________________________________
# Q47. Remove Duplicate Words
# Write a function that removes duplicate words while preserving their original order.
# Input:
# "python is easy python is powerful"
# Output:
# "python is easy powerful"
# ________________________________________
# Q48. Reverse Every Word
# Write a function that reverses each word but keeps the word order.
# Input:
# "Python is easy"
# Output:
# "nohtyP si ysae"
# ________________________________________
# 🔥 List Logic
# Q49. Separate Numbers
# Write a function that rearranges the list into:
# 1.	Positive numbers
# 2.	Negative numbers
# 3.	Zeros
# Maintain the original order inside each group.
# Input:
# [0, -5, 3, 8, -2, 0, 4, -1]
# Output:
# [3, 8, 4, -5, -2, -1, 0, 0]
# ________________________________________
# Q50. Find Unique Elements
# Write a function that returns elements appearing exactly once.
# Input:
# [1, 2, 2, 3, 4, 4, 5, 6, 6]
# Output:
# [1, 3, 5]
# ________________________________________
# Q51. Find Duplicate Elements
# Write a function that returns elements appearing more than once.
# Input:
# [1, 2, 3, 2, 4, 1, 5, 3]
# Output:
# [1, 2, 3]
# ________________________________________
# Q52. Second Largest Unique
# Find the second-largest unique number without using sort() or sorted().
# Input:
# [10, 20, 5, 20, 15, 10, 8]
# Output:
# 15
# ________________________________________
# Q53. Move Zeros
# Move all zeros to the end while maintaining the order of non-zero elements.
# Input:
# [0, 3, 0, 5, 2, 0, 8]
# Output:
# [3, 5, 2, 8, 0, 0, 0]
# ________________________________________
# Q54. Rotate List
# Write a function that moves the last k elements to the beginning.
# Input:
# [1, 2, 3, 4, 5, 6]
# k = 3
# Output:
# [4, 5, 6, 1, 2, 3]
# ________________________________________
# 🧩 Nested List Questions
# Q55. Nested List Analysis
# Given:
# numbers = [
#     [10, 20],
#     [5, 15, 25],
#     [30, 40]
# ]
# Find:
# 1.	Total number of elements
# 2.	Sum of all elements
# 3.	Largest element
# 4.	Smallest element
# Condition: Don't use sum() or max() or min().
# ________________________________________
# Q56. Find Largest Sublist Sum
# Given:
# numbers = [
#     [1, 2, 3],
#     [10, 5],
#     [4, 6, 8]
# ]
# Find the sublist having the largest sum.
# Expected:
# [4, 6, 8]
# ________________________________________
# Q57. Flatten a Nested List
# Convert:
# [[1, 2], [3, 4], [5, 6]]
# into:
# [1, 2, 3, 4, 5, 6]
# Condition: Don't use any built-in flattening function.
# ________________________________________
# 🔥 Higher-Order Function Questions
# Q58. Square Even Numbers
# Use filter() and map() to find the squares of even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [4, 16, 36]
# ________________________________________
# Q59. Filter Names
# Use filter() and lambda to return names that:
# •	start with "A"
# •	length > 4
# Input:
# ["Anu", "Anjali", "Arjun", "Akhil", "Binu", "Amal"]
# Output:
# ["Anjali", "Arjun", "Akhil"]
# ________________________________________
# Q60. Product Using Reduce
# Use reduce() to find the product of all numbers.
# Input:
# [2, 3, 4, 5]
# Output:
# 120
# ________________________________________
# Q61. Largest Using Reduce
# Use reduce() to find the largest number.
# Input:
# [12, 45, 7, 23, 56, 18]
# Output:
# 56
# ________________________________________
# Q62. Filter and Transform
# Given:
# numbers = [5, 12, 7, 18, 20, 3, 25]
# Using filter() and map():
# 1.	Select numbers greater than 10
# 2.	Find their squares
# Expected:
# [144, 324, 400, 625]
# ________________________________________
# ⭐ Mini Exam Challenge
# Q63. Complete Number Analyzer
# Write a function:
# number_analyzer(lst)
# that returns a dictionary:
# {
#     "even": ...,
#     "odd": ...,
#     "zero": ...,
#     "largest": ...,
#     "smallest": ...,
#     "average": ...
# }
# For:
# [10, 0, 5, 8, 0, 3, 12, 7]
# ________________________________________
# Q64. Student Performance Analyzer
# Write:
# student_analysis(marks)
# For:
# [35, 78, 45, 90, 22, 56, 88]
# return:
# Highest
# Lowest
# Average
# Passed count
# Failed count
# Second highest
# Passing mark = 40.
# ________________________________________
# Q65. ⭐ Combined Logic Question
# Write a function:
# analyze_list(lst)
# that returns:
# •	numbers appearing once
# •	duplicate numbers
# •	largest
# •	second largest
# •	smallest
# •	even count
# •	odd count
# •	zero count
# Input:
# [4, 2, 7, 2, 0, 5, 4, 8, 0, 9]
# SET 5
# 🔥 Python Core Coding Practice Set
# 🟢 Basic → Intermediate
# Q1. Vowel Counter
# Write a function that accepts a string and returns the total number of vowels in it.
# Input: "Python Programming"
# Output: 4
# Condition: Treat uppercase and lowercase vowels the same.
# ________________________________________
# Q2. Vowel Frequency
# Write a program to find the frequency of each vowel in a string.
# Input: "education"
#
# Output:
# a : 1
# e : 1
# i : 1
# o : 1
# u : 1
# ________________________________________
# Q3. Move Zeros
# Write a function that moves all zeros to the end of a list while maintaining the order of the other elements.
# Input:  [0, 5, 0, 3, 4, 0, 2]
#
# Output: [5, 3, 4, 2, 0, 0, 0]
# ________________________________________
# Q4. Most Frequent Element
# Write a function that returns the element occurring the maximum number of times.
# Input:  [4, 1, 2, 1, 2, 1, 5]
#
# Output: 1
# ________________________________________
# Q5. Character Frequency
# Write a program to count the frequency of every character using a dictionary.
# Input: "programming"
#
# Output:
# {
#     'p': 1,
#     'r': 2,
#     'o': 1,
#     'g': 2,
#     'a': 1,
#     'm': 2,
#     'i': 1,
#     'n': 1
# }
# Ignore spaces.
# ________________________________________
# 🔵 Palindrome / String Logic
# Q6. String Palindrome
# Write a function to check whether a string is a palindrome.
# Input: "madam"
# Output: True
# Input: "python"
# Output: False
# Condition: Don't use [::-1].
# ________________________________________
# Q7. Number Palindrome
# Write a program to check whether a number is a palindrome.
# Input: 121
# Output: True
# Input: 123
# Output: False
# Condition: Don't convert the number to a string.
# ________________________________________
# Q8. Anagram
# Write a function to check whether two strings are anagrams.
# Input:
# "listen"
# "silent"
#
# Output:
# True
# Another example:
# Input:
# "hello"
# "world"
#
# Output:
# False
# ________________________________________
# Q9. Anagram Without sorted()
# Check whether two strings are anagrams without using sort() or sorted().
# Input:
# "triangle"
# "integral"
#
# Output:
# True
# ________________________________________
# 🟣 Prime Number / Number Logic
# Q10. Prime Number
# Write a function that checks whether a given number is prime.
# Input: 17
# Output: True
# Input: 20
# Output: False
# ________________________________________
# Q11. Prime Numbers in a Range
# Write a program to print all prime numbers between 1 and 50.
# Output:
# 2 3 5 7 11 13 17 ...
# ________________________________________
# Q12. Count Prime Numbers
# Write a function that counts how many prime numbers are present in a list.
# Input: [2, 4, 5, 7, 9, 11, 15]
#
# Output: 4
# ________________________________________
# 🟠 Second Largest / List Logic
# Q13. Second Largest
# Find the second-largest unique element without using sort() or sorted().
# Input: [10, 5, 8, 10, 3, 8]
#
# Output: 8
# ________________________________________
# Q14. Second Smallest
# Find the second-smallest unique element without using sort().
# Input: [8, 3, 5, 3, 1, 8, 2]
#
# Output: 2
# ________________________________________
# Q15. Largest and Smallest
# Find the largest and smallest elements without using max() and min().
# Input: [15, 4, 20, 8, 2]
#
# Output:
# Largest: 20
# Smallest: 2
# ________________________________________
# 🟡 Factorial / Functions
# Q16. Factorial Using Function
# Define:
# factorial(n)
# and return the factorial of a number.
# Input: 5
# Output: 120
# ________________________________________
# Q17. Factorial Using Loop
# Write a program to find the factorial of a number using a loop.
# Condition: Don't use math.factorial().
# ________________________________________
# Q18. Factorial of Numbers in a List
# Write a function that accepts a list and returns the factorial of every number.
# Input: [2, 3, 4, 5]
#
# Output: [2, 6, 24, 120]
# ________________________________________
# 🔥 Armstrong Number
# Q19. Armstrong Number
# Write a program to check whether a number is an Armstrong number.
# Input: 153
# Output: True
# Because:
# 1³ + 5³ + 3³ = 153


# ________________________________________
# Q20. Armstrong Numbers in a Range
# Print all Armstrong numbers between 1 and 1000.
# ________________________________________
# Q21. Armstrong Function
# Define:
# is_armstrong(n)
# that returns True if the number is Armstrong, otherwise False.
# ________________________________________
# 🟢 Looping Questions
# Q22. Sum of Digits
# Find the sum of digits without converting the number into a string.
# Input: 5832
# Output: 18
# ________________________________________
# Q23. Reverse a Number
# Reverse a number using a loop.
# Input: 12345
# Output: 54321
# ________________________________________
# Q24. Count Digits
# Count the number of digits in an integer.
# Input: 58392
# Output: 5
# ________________________________________
# Q25. Multiplication Table
# Write a program to print the multiplication table of a given number.
# Input: 5
#
# Output:
# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 10 = 50
# ________________________________________
# Q26. Fibonacci Series
# Print the first n terms of the Fibonacci series.
# Input: 7
#
# Output:
# 0 1 1 2 3 5 8
# ________________________________________
# 🔥 Pattern Printing
# Q27. Number Pattern
# For n = 5:
# 1
# 12
# 123
# 1234
# 12345
# ________________________________________
# Q28. Repeated Number Pattern
# For n = 5:
# 1
# 22
# 333
# 4444
# 55555
# Condition: Try using string repetition.
# ________________________________________
# Q29. Continuous Number Pattern
# For n = 4:
# 1
# 23
# 456
# 78910
# ________________________________________
# Q30. Reverse Pattern
# For n = 5:
# 12345
# 1234
# 123
# 12
# 1
# ________________________________________
# Q31. Number Palindrome Pattern
# For n = 5:
#     1
#    121
#   12321
#  1234321
# 123454321
# ________________________________________
# 🔥 Dictionary / Frequency
# Q32. Word Frequency
# Write a program using a dictionary to count the frequency of each word.
# Input:
# "python is easy python is powerful"
#
# Output:
# {
#     "python": 2,
#     "is": 2,
#     "easy": 1,
#     "powerful": 1
# }
# ________________________________________
# Q33. Number Frequency
# Count the frequency of each number using a dictionary.
# Input:
# [2, 3, 2, 4, 3, 2]
#
# Output:
# {
#     2: 3,
#     3: 2,
#     4: 1
# }
# ________________________________________
# Q34. First Non-Repeating Character
# Using a dictionary, find the first character that occurs only once.
# Input: "aabbcddee"
#
# Output: c
# ________________________________________
# 🚀 Higher-Order Functions
# Q35. Map — Square Numbers
# Use map() to find the square of every number.
# Input:
# [1, 2, 3, 4, 5]
#
# Output:
# [1, 4, 9, 16, 25]
# ________________________________________
# Q36. Filter — Even Numbers
# Use filter() to extract only even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
#
# Output:
# [2, 4, 6]
# ________________________________________
# Q37. Filter — Numbers Greater Than 10
# Use filter() and lambda.
# Input:
# [5, 12, 7, 18, 20, 3]
#
# Output:
# [12, 18, 20]
# ________________________________________
# Q38. Map + Filter
# Use filter() to select even numbers and map() to find their squares.
# Input:
# [1, 2, 3, 4, 5, 6]
#
# Output:
# [4, 16, 36]
# ________________________________________
# Q39. Reduce — Product
# Use reduce() to calculate the product.
# Input:
# [2, 3, 4, 5]
#
# Output:
# 120
# ________________________________________
# Q40. Reduce — Largest
# Use reduce() to find the largest number.
# Input:
# [10, 25, 5, 40, 15]
#
# Output:
# 40
# ________________________________________
# 🔥 Functions + Multiple Concepts
# Q41. Number Analyzer
# Write:
# analyze_numbers(lst)
# The function should return:
# •	largest
# •	smallest
# •	average
# •	even count
# •	odd count
# Example:
# Input:
# [10, 5, 8, 3, 12]
#
# Output:
# Largest: 12
# Smallest: 3
# Average: 7.6
# Even: 3
# Odd: 2
# ________________________________________
# Q42. String Analyzer
# Write:
# analyze_string(s)
# Return:
# •	number of vowels
# •	number of consonants
# •	number of digits
# •	number of spaces
# •	longest word
# ________________________________________
# Q43. List Analyzer
# Write:
# analyze_list(lst)
# Return:
# •	unique elements
# •	duplicate elements
# •	largest
# •	second largest
# •	even count
# •	odd count
# Example:
# Input:
# [4, 2, 7, 2, 5, 4, 8, 9]
# ________________________________________
# Q44. Student Result
# Write:
# student_result(marks)
# Return:
# •	highest mark
# •	lowest mark
# •	average
# •	passed count
# •	failed count
# Passing mark = 40.
# Input:
# [35, 78, 45, 90, 22, 56]
#
# Output:
# Highest: 90
# Lowest: 22
# Average: ...
# Passed: 4
# Failed: 2
# ________________________________________
# Q45. ⭐ Final Combined Challenge
# Write a function:
# analyze(lst)
# For a list of integers, return a dictionary containing:
# {
#     "even": number_of_even,
#     "odd": number_of_odd,
#     "zero": number_of_zero,
#     "largest": largest_number,
#     "smallest": smallest_number,
#     "second_largest": second_largest_unique,
#     "unique": elements_appearing_once
# }
# Example:
# Input:
# [4, 2, 7, 2, 0, 5, 4, 8, 0, 9]
#
#

#Qn Swap
a,b=1,3
a,b=b,a
print("a =",a ,"\nb =",b)

# 5. String Concatenation
# Create two variables:
#
first_name="Bidhya"
last_name="P T"
# # Join them and print the full name.

full_name=first_name+" "+last_name
print(full_name)

# 6. String Repetition
# Print "Python " 5 times using the repetition operator.
# Expected:
# Python Python Python Python Python

print("Python "*5)



# Q7
# Create a function using *args that finds the largest number.
# def largest(*args):
#     large=args[0]
#     for i in args:
#         if i>large:
#             large=i
#     print(large," is largest")
#     return
# largest(2,7,9)
#
# for i in range(1,6):
#     print(" "*(5-i),end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#
#     print()
#
# for i in range(4,0,-1):
#     print(" " * (5 - i), end="")
#     for j in range(1, i + 1):
#         print("* ", end="")
#
#     print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

num=153
s=str(num)
digit_sum=0



