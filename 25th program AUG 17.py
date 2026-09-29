# Define a function that takes a list of numbers
#
# as argument and print the count of even numbers,
# odd numbers and numbers whose value greater than 50
#
l=[23,56,12,78,98,89,31,67]

def count(list):
    even_count = 0
    odd_count = 0
    greater_than_50 = 0

    for i in list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if i > 50:
            greater_than_50 += 1

    print(f"Even numbers count: {even_count}")
    print(f"Odd numbers count: {odd_count}")
    print(f"Numbers greater than 50 count: {greater_than_50}")

count(l)

#Qn 2. Define a function that takes a list of words as arguments
#and returns a new list of lengths


l = ["red", "green", "orange", "yellow", "blue"]


def lengths(words):
    new = []
    for i in l:  # Use 'words' instead of 'l'
        new.append(len(i))
    return new  # Move outside the loop and return the list


print(lengths(l))  # Output: [3, 5, 6, 6, 4]


           ##########################

   #Lambda functions

#Define a function that takes a number as argument and return
#its square.

#User defined
def square(number):
    return number**2


a=square(5)
print(a)  # Output: 25

#Lambda

s=lambda n:n**2
print(s(5))

#Define a lambda function to find the cube of a number

s=lambda n:n**3

print(s(5))

            ###############################
# Qn 1.sum of 2 numbers
s=lambda a,b:a+b
print(s(4,6))


# Qn 2.product of 3 numbers
s=lambda a,b,c:a*b*c
print(s(2,3,4))


# Qn 3.length of a string

s=lambda a:len(a)
print(s("python"))


#Qn 4.square root of a number
s=lambda a:int(a**0.5)
print(s(25))

#Qn 5.first letter of a string
s=lambda a:a[0]
print(s("python"))

#Qn 6.last letter of a string
s=lambda a:a[-1]
print(s("python"))

#Qn 7.name value from dictionary
a= {"name": "Anu", "salary": 50000}
s= lambda d: d["name"]
print(s(a))

   # OR

s=lambda a:a.get("name")
print(s(a))

#Qn 8.salary value from dictionary
a= {"name": "Anu", "role": "Developer", "salary": 50000}
s = lambda d: d["salary"]
print(s(a))

          #OR

s = lambda a: a.get("salary")
print(s(a))

#Qn.9 add 10 to a number

s=lambda a:a+10
print(s(4))




              #####################################
#Map
l=[1,2,3,4]

#create a new list of squares

#map(function,sequence)

print(map(lambda x:x**2,l)) #object formate

print(list(map(lambda x:x**2,l))) # List value
print(set(map(lambda x:x**2,l))) # Set value
print(tuple(map(lambda x:x**2,l))) # Tuple value






