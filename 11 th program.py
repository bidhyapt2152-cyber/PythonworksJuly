# #Iterating Through a String
# s='hello'
# for i in s:
#     print(i)

# #Iterating Over a List
# l=[1,2,3,4]
# for i in l:
#     print(i)

#Iterating Over Tuple
# t=(1,2,3,4)
# for i in t:
#     print(i)

# Iterating Over set
# s={1,2,3,4,5}
# for i in s:
#     if i%2==0:
#         print(i)
#     else:
#         print()

#print each colors=['red','green','blue']
# l=['red','green','blue']
# for i in l:
#     print(i)

#Iterating Over dictionary
# d={'a':10,'b':20,'c':30}
# for i in d:
     #print(i)


   # print(i,":",d[i])

#Print sum of numbers in list [56,89,34,10]
# l=[56,89,34,10]
# s=0
# for i in l:
#     s=s+i
# print(s)

#Reverse without using slicing
# s='malayalam'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)
#
# if s==rev:
#     print( 'is palindrome')
# else:
#     print( 'is not palindrome')

#Reverse of a number
# n=1034
# rev=''
# s=str(n)
# for i in s:
#     rev=i+rev
# print(rev)

#l=[12,34,56,45,89,16,69,33]
#print each number in a list
# for i in l:
#     print(i)

#print even values
# for i in l:
#     if i%2==0:
#         print(i)
#
#print those numbers that are divisible by 5
# for i in l:
#     if i%5==0:
#         print(i)

#print those numbers that contains digit 3
# for i in l:
#     if '3' in str(i):
#         print(i)


#sum of list
# s=0
# for i in l:
#     s=s+i
# print(s)


#count of even numbers in the list
# count=0
# for i in l:
#      if i%2==0:
#          count=count+1
# print(count)

#product of the list
# p=1
# for i in l:
#     p=p*i
# print(p)
#squares

# for i in l:
#     i=i**2
# print(i)


# l=[12,4,5,6.8,30,'arun','hello']
# #print only float point values
# for i in l:
#     if type(i)==float:
#         print(i)
#
# #print only string values
# for i in l:
#     if type(i)==str:
#         print(i)
#
# #print only  numbers
# for i in l:
#     if type(i)==int:
#         print(i)

#d={'a':23,'b':25,'c':28,'d':30,'e':22}
# #even values
# for i in d.values():
#     if i%2==0:
#         print(i)
colors = ['red', 'green', 'blue', 'orange', 'black']
#starting letter
# for i in colors:
#     i=i[0]
#     print(i)
#last letter
# for i in colors:
#     i=i[-1]
#     print(i)
#reverse
# rev=''
# for i in colors:
#     rev=i+rev
# print(rev)

#all colors containing letter b

colors = ['red', 'green', 'blue', 'orange', 'black']

# Check each color
for color in colors:
    if 'b' in color:
        print(color)

