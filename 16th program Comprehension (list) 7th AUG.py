#List comprehension
# Qn 1
# Given a list
# l=[1,2,3,4]


# Qn. create a new list with squares of each element
# new=[]                        #Normal method
# for i in l:
#     new.append(i**2)
# print(new)
#
#          #OR                  # Comprehension
# new=[i**2 for i in l]         # in each iteration ADDS i**2 where i takes value from sequence l
# print(new)



# Qn  create a new list with cubes of each element
# new=[]                           #Normal method
# for i in l:
#     new.append(i**3)
# print(new)

      #OR
                         # Comprehension
# new=[i**3 for i in l]    # in each iteration ADDS i**2 where i takes value from sequence l
# print(new)



# Qn  create a new list which add 5 to each element
# new=[]
# for i in l:
#     new.append(i+5)
# print(new)

          # OR
# new=[i+5 for i in l]
# print(new)

# Qn  create a new list which change each element to 5
# new=[]
# for i in l:
#     new.append(5)
# print(new)
#
#       # OR
#
# new=[5 for i in l]
# print(new)
# #
#
                  #############################################
#  Qn 2

# #Given a list
# l=[23,46,55,11,78,90,24]
#
# # Qn  create a new list with even values
# new=[]
# for i in l:
#     if i%2==0:
#         new.append(i)
# print(new)
#
#
#         #OR
# new=[i for i in l if i%2==0]
# print(new)
#
#
# # Qn create a  new list with numbers whose value is greater than 50
# new=[]
# for i in l:
#     if i>50:
#         new.append(i)
# print(new)
#
#      # OR
# new=[i for i in l if i>50]
# print(new)
#
#
#                  ############################################################################
# # Qn. 3
# # Given a list
# l=[12,45,34,67,90]
#
# # Qn. create a new list with even values
# new=[]
# for i in l:
#     if i%2==0:
#         new.append(i)
# print(new)
#
#       #OR
# new=[i for i in l if i%2==0]
# print(new)
#
#
# # Qn create a new list with values greater than 50
# new=[]
# for i in l:
#     if i>50:
#         new.append(i)
# print(new)
#
#  # OR
# new=[i for i in l if i>50]
# print(new)
#
#              #########################################
#
# # Qn 4
#
# # #Given  a list
# colors=['red','green','blue','orange']
#
# # Qn create a new list with first letter of each color
# new=[]
# for i in colors:
#     new.append(i[0])
# print(new)
#
#
#       #OR
# new=[i[0] for i in colors]
# print(new)
#
# # Qn  create a new list with length of each color
# new=[]
# for i in colors:
#     new.append(len(i))
# print(new)
#
#
# new=[len(i) for i in colors ]
# print(new)
#


# Qn create a new list of cubes
# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**3)
# print(new)
#
#      # OR
# new=[i**3 for i in l]
# print(new)

                    ################################################
#
# # Qn.5 create a new list of square roots
# l=[25,36,81,100]
#
# # new=[]
# # for i in l:
# #     new.append(i**2)
# # print(new)
#
#    #OR
# # new=[i**2 for i in l]
# # print(new)
#
#
#                       ##############################################
#
#
# # Qn.6  create a new list of lengths
#
# colors=['red','green','blue','yellow','black']
#
# new=[]
# for i in colors:
#     new.append(len(i))
# print(new)
#
#     #OR
# new=[len(i) for i in colors]
# print(new)
#
#
# # Qn create a new list of first characters
# new=[]
# for i in colors:
#     new.append(i[0])
# print(new)
#
#     #OR
#
# new=[i[0] for i in colors]
# print(new)
#
#
# # Qn create a new list of last characters
# new=[]
# for i in colors:
#     new.append(i[-1])
# print(new)
#
#
#       #OR
# new=[i[-1] for i in colors]
# print(new)
#
#
# # Qn create a new list of reverse of each element
# new=[]
# for i in colors:
#     new.append(i[::-1])
# print(new)
#
#         #OR
# new=[i[::-1] for i in colors]
# print(new)

             #################################


# Qn.7 Given a list
#l=[23,78,12,56]

# # #Add 10 to each element in the given sequence
# new=[]
# for i in l:
#     new.append(i+10)
# print(new)
#
#     #OR
# new=[i+10 for i in l]
# print(new)

             ##################################
 # Qn.8
# #given a list of dictionaries
#l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
     # {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
     # {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# Qn create a new list of emails
# new=[]
# for i in l:
#     new.append(i['email'])
# print(new)
#
#
#    #OR
# new=[i['email'] for i in l]
# print(new)

            ###########################################3

#  Qn.9
 # Qn create a new list with square root of each element
# l=[25,16,9,36]
# new=[]
# for i in l:
#     new.append(int(i**0.5))           #List cannot be directly converted to integer
# print(new)
#
#   # OR
# new=[int(i**0.5) for i in l]
# print(new)

            ###################################################


# Qn.10 Given a dictionary

#d={'arun':25,'amal':34,'akhil':26,'anu':21}

# Qn create a list of names
# new=[]
# for i in d:
#     new.append(i)
# print(new)
#
#   #OR
#
# new=[i for i in d]
# print(new)

#Qn  create a list of marks
# new=[]
# for i in d:
#     new.append(d[i])              #d[i] >> gives values of corresponding keys
# print(new)
#
#      #OR
# new=[d[i] for i in d]
# print(new)


             ################################

# Qn.11 Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # Qn create a list of string values
# new=[]
# for i in l:
#     if type(i)==str:          #Type should be declared >>could not convert string to float
#         new.append(i)
#
# print(new)
#
#    # OR
# new=[i for i in l if type(i)==str]
# print(new)
#
#
# # Qn. create a list of floats
# new=[]
# for i in l:
#     if type(i)==float:
#         new.append(i)
# print(new)
#
#
#     # OR
# new=[i for i in l if type(i)==float]
# print(new)
#
# # Qn create a list of positive numbers
# new=[]
# for i in l:
#     if type(i)!=str and i>0:
#         new.append(i)
# print(new)
#
#           #OR
# new=[i for i in l if type(i)!=str and i>0]
# print(new)

                 #########################################

# Qn.12
# Given a list

fruits=['apple','orange','pineapple','avocado','grapes']

# Qn. create a new list with elements whose length is greater than 6
# new=[]
# for i in fruits:
#     if len(i)>6:
#         new.append(i)
# print(new)
#
#  #OR
#
# new=[i for i in fruits if len(i)>6]
# print(new)

                 ###############################################


# Qn.13  create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[]
# for i in range(1,101):
#     if i%3==0:
#         new.append(i)
# print(new)
#
#  #OR
# new=[i for i in range(1,101) if i %3==0]
# print(new)


              #######################################
# Qn.14
# Given
s="python coding  is easy and fun"

# Qn. create a new list with only vowels
new=[]
v='AEIOUaeiou'
for i in s:
    if i in v:
        new.append(i)
print(new)

    #OR
new=[i for i in s if i in 'AEIOUaeiou']
print(new)