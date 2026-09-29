# Q.Write Python Programs Using map(), filter(), or reduce()

# 1.Capitalize all names in a list

names = ['alin', 'arun', 'anu']
print(list(map(lambda x:x.capitalize(),names)))

              ######################################

# 2.Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
print(list(map(lambda x:x+"@gmail.com",users)))
#

                 ###################################


# 3.Filter out all empty strings from a list

words = ['hello', ' ', 'world', ' ', 'python']
print(list(filter(lambda x:x.isspace(),words)))

               #####################################

# 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(list(filter(lambda x:x[0]=='A',names)))

              #####################################

# 5.Concatenate all strings in a list
words = ['Python', 'is', 'fun']
import functools
print(functools.reduce(lambda a,b:a+" "+b,words))

                ###############################

# 6.Multiply all numbers in a list
nums = [2, 3, 4]
import functools
print(functools.reduce(lambda a,b:a*b,nums,1))

              #################################

# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
print(list(map(lambda x:x[0],words)))


             #################################


# 8.Add 10 to Each Number
nums = [5, 10, 15]
print(list(map(lambda x:x+10,nums)))

                 ###################################

# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
new=[]
for i in l:
    if i>=1 and i%2==0:
        new.append(i)
import functools
print(functools.reduce(lambda a,b:a+b,new))

    # #Sum of Positive Odd numbers
new=[]
for i in l:
    if i>=1 and i%2!=0:
        new.append(i)
import functools
print(functools.reduce(lambda a,b:a+b,new))


     ####OR


from functools import reduce

l = [12, -4, 78, -34, 90, 45, 16, 26, -2, -11, 3]

# Step 1: Filter numbers that are both positive (> 0) and even (% 2 == 0)
positive_evens = filter(lambda x: x > 0 and x % 2 == 0, l)

# Step 2: Reduce the filtered list by adding the elements together
result = reduce(lambda x, y: x + y, positive_evens, 0)

print("Sum of positive even numbers:", result)


    # #Sum of Negative  odd numbers
new=[]
for i in l:
    if i<0 and i%2!=0:
        new.append(i)

import functools

print(functools.reduce(lambda a,b:a+b,new))

    # #Sum of Negatve Even numbers
new=[]
for i in l:
    if i<0 and i%2==0:
        new.append(i)
import functools
print(functools.reduce(lambda a,b:a+b,new))

    # #Count of Positive numbers
print(len(list(filter(lambda x: x>0,l))))

    # #Count of negative numbers
print(len(list(filter(lambda x: x<0,l))))

                 ##############################

# 10.Given a list
nums = ["1", "2", "3", "4"]

# Convert all Strings to Integers [1,2,3,4]
print(list(map(lambda x:int(x),nums)))


              ########################################
# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
print(list(map(lambda x:x['name'].capitalize(),p)))

#print products with price greater than 10000
print(list(filter(lambda x: x['price']>10000,p)))

#Find the total price of all products
import functools
print(functools.reduce(lambda a,b: a+b['price'],p,0))