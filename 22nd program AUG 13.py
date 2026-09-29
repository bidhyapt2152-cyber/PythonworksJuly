# Qn 1. Write a program to find the position of a specific character in a string

s="hello world"
ch="y"
if ch in s:
    print("The position of",ch,"is",s.index(ch))
else:

    print("The position of", ch, "is not present")


            ############################################

# Qn 2. Write a program to find the count of a special character in a string
#
s="hello world"
ch="y"
print("The count of",ch,"is",s.count(ch))

                #####################################

# Qn 3. Write a program to create the dictionary  where keys are letters and values are the count of each letter

new={}
for i in s:
    if i.isalpha():
        new[i]=s.count(i)
print(new)

                ##################################################3

# 4.Qn write a program to create new list with 5 random 3 digit number
import random
new=[]
for i in range(5):
        n=random.randint(100,1000)
        new.append(n)
print(new)

                         ############################################3

# Qn. 5 write a program to create a 5 digit otp number
print(random.randint(10000,100000))

                 ##########################################################

# Qn 6 write a program to find the count of letters,spaces and digits in a string
s="hello world"
count_l=0
count_d=0
count_sp=0
for i in s:
    if i.isalpha():
        count_l+=1
    elif i.isspace():
        count_sp+=1
    elif i.isdigit():
        count_d+=1
print("count of letters",count_l)
print("count of space", count_sp)
print("count of digit", count_d)


