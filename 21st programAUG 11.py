#Define a function that takes string as argument and return a new dictionary where keys are words and values are length
# of each word call the function and print the dictionary

# s="Python coding is easy and fun"
#
# # def dict(str):
# #     new = {i: len(i) for i in str.split()}
# #     return new
# # a=dict(s)
# # print(a)
#
#   ################### TYPES OF FUNCTIONAL ARGUMENTS   #######################
#
#
# #### 1. Positional Arguments
# #example:
# def fun(n,a):
#
#      print("name",n)
#      print("age",a)
#
#      return
# fun("arun",23)
#
#
# #### 2. Keyword Arguments
# #example:
# def fun(n, a):
#
#     print("name", n)
#     print("age", a)
#
#     return
#
#
# fun(n="arun",a= 23)
# fun(a= 23,n="arun")


#### 3. Default Arguments
# example:
# def fun(n, a=23):               #Set default age value
#
#     print("name",n)
#     print("age",a)
#
#     return
#
#
# fun(n="arun")



#### 4. Variable length\ Arbitary Arguments
# example:
# def fun(a,b):
#     print(a,b)
#
#
#     return
#
#
# fun(10,20)



#### i) Variable length\ Arbitary   positional Arguments
#
# def fun(*args):
#     print(args)
#
#
#     return
#
#
# fun(10,20)
#fun(10,20,30)


#### ii) Variable length\ Arbitary keyword Arguments
# def fun(**kwargs):
#     print(kwargs)
#
#
#     return
#
# fun(a=10,b=20)
#
# fun(a=10,b=20,c=30)


               ############################
#Qn
def add(*args):
    a=sum(args)
    print(a)


    return
add(2,3)
add(2,3,4)
add(10,20,30,40,50)


  #OR
def add(*args):
    for i in args:
        i
