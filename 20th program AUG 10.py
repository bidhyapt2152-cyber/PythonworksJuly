# Qn.  Sum of two numbers (using parameters and argments)


# def add(n1,n2):
#     s=n1+n2
#     print("Sum is",s)
#
#     return
# add(12,8)                               #Static
#
#        #OR

# def add(n1,n2):
#     s=n1+n2
#     print("Sum is",s)
#
#     return
#
# a=int(input("Enter the first number:"))         #Dynamic
# b=int(input("Enter the second number:"))
#
# add(a,b)


                   ##########################################


# Qn. Define a function that takes 3 arguments and find simple interest (dynamic input)

# def si(p,n,r):
#     s=p*n*r/100                                            #Simple Intrest
#     print("SI is",s)
#     return
#
# a=float(input("Enter the principle amount:"))
# b=float(input("Enter the years:"))
# c=float(input("Enter th rate:"))
# si(a,b,c)

                     ################################


#Define a function that takes string and a character as arguments and print the count


# def count_ch(st,ch):
#      count=0
#
#      for i in st :
#          if i==ch:
#              count=count+1
#      print(count)
#
#      return
#
# s=input('Enter the string:')
# ch=input('Enter the character:')
# count_ch(s,ch)



           ####################################

#Return statemets

# def add(n1,n2):
#     s=n1+n2
#
#
#     return
# a=add(12,8)
# print(a)
#
#
# def add(n1,n2):
#     s = n1 + n2
#     return s
# a=add(12,8)
# print(a)

               ######################################


#Define a function that takes 3 numbers and return the product as result call the function and print the product

def pro(n1,n2,n3):
    p=n1*n2*n3

    return p
a=pro(1,2,3)
print(a)
