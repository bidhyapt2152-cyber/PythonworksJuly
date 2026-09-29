# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(n1,n2):
#     p=n1*n2
#
#     return p
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
#
#
# a=product(n1,n2)
# print(a)
#


       #################################################


# # Q2.Define a function that takes a string and returns number of vowels
# def vowels(s):
#
#     v="aeiouAEIOU"
#     count=0
#     for i in s:
#         if i in v:
#             count=count+1
#     return  count
#
# s=input("Write a string:")
# a=vowels(s)
# print(a)


       #####################################################


#
# # Q3.Define a function that takes length and breadth and returns area of rectangle
# def area(l,b):
#     a=l*b
#
#     return a
# l=int(input("Enter the length:"))
# b=int(input("Enter the breadth:"))
# c=area(l,b)
# print(c)


                  ##############################################
#
# # Q4.Define a function that takes a list of numbers and creates a new list with even numbers and returns the new list
# l=[45,78,90,12,35]
# def new_list(lst):
#     new = [i for i in lst if i%2==0]
#     return new
#
#
# a=new_list(l)
# print(a)


                    ###############################################3


# # #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # # each value is the sum of digits of corresponding number in the original list.
l = [123, 345, 111, 678, 134, 809]
def sum_digits(lst):
    new=[sum(int(i) for i in str(i)) for i in lst]
    return new


a=sum_digits(l)
print(a)
#
#
#
#            #OR
#
# def new():
#     new=[]
#     for i in l:
#         s=str(i)
#         sum=0
#         for j in s:
#             sum=sum+int(j)
#         new.append(sum)
#     print(new)
#     return
# new()




                 #################################################



#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list

#
l=[12,34,78,12,67,34,90,23]
def unique(elements):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    return new
a=unique(l)
print(a)

                #####################################################


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
list1=[12,34,56,78,90]
list2=[90,34,11,57,45]
# new=[]
# def common(list1,list2):
#     new=[i for i in list1 if i in list2]
#
#     return new
# a=common(list1,list2)
# print(a)





