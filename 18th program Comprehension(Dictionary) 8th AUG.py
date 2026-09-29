
# Qn 1
#Given list
# l=[1,2,3,4]
# #Create a new dictionary where keys are numbers and values the squares of each number
# #out= {1:1,2:4,3:9,4:16}
#
# new={}                      #Normal method
# for i in l:
#     new[i]=i**2
# print(new)
#
#
#    #OR
# new={i:i**2 for i in l}
# print(new)
#
#
#             #####################################################
#
# #Qn.2
# # #Given list
# l=[1,2,3,4]
#
# # Qn Create a new dictionary where keys are numbers and values the cubes of each number
# new={}
# for i in l:
#     new[i]=i**3
# print(new)
#
#
#  #OR
#
# new={i:i**3 for i in l}
# print(new)

#
#           ###########################################################


#  Qn.3
# #Given a list
l=[10,20,30,40]

# Qn Create a new dictionary where keys are index and values are number itself
new={}
for i in range(len(l)):     # range(len(i)) is saved as key values
    new[i]=l[i]
print(new)

  #OR
new={i:l[i] for i in range(len(l))}
print(new)

#
#              ######################################################


    ######## string.split()

# Qn.
# # Given string
s='python coding is easy and fun'
#
# Print each word
for i in s.split():
    print(i)


#
#                ####################################################
#
# Qn.4 Given string
s ='python coding is easy and fun'
#
# Qn. Create a new dictionary where keys are words and values are length of each word.
new={}
for i in s.split():
     new[i]=len(i)
print(new)

 #OR

new={i:len(i) for i in s.split()}
print(new)

