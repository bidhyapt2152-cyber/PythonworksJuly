#Write a program to print first 10 integers
#Initialisation
# i=1                      #var for looping is i. starting from 1
# while i<=10:             # upto 10
#    # print(i)
#    print(i,end=" ")      # to print integers horizontally
#    i+=1

# #Write a program to print first 10 even numbers
# i=2
# while i<=20:
#     print(i,end=", ")
#     i+=2



#Write a program to print first 10 odd numbers
# i=1
# while i<=20: #loop condition.
#     print(i,end=", ")
#     i+=2

#Write a program to print 3,6,9,12,15,18,21
# i=3
# while i<=21: #loop condition.
#     print(i,end=", ")
#     i+=3

#Write a program to print 5,4,3,2,1
# i=5
# while i>=(1): #loop condition.
#     print(i,end=", ")
#     i-=1

#Write a program to print 1,4,7,10,13,16
# i=1
# while i<=16: #loop condition.
#     print(i,end=", ")
#     i+=3

#Write a program to print 10,20,30,40,50,60,70,80
# i=10
# while i<=80: #loop condition.
#     print(i,end=", ")
#     i+=10

#Write a program to print 8,6,4,2,0
# i=8
# while i>=0: #loop condition.
#      print(i,end=", ")
#      i-=2

#Write a program to print 100,101,102,....200
# i=100
# while i<=200:
#     print(i, end=", ")
#     i+=1
#Write a program to print all 4 digit numbers (1000-9999)
#i=1000
# while i<=9999:
#     print(i, end=", ")
#     i+=1

#Write a program to print all 3 digit numbers that are divisible by 3
# i=100
# while i<=999:
#     if i%3==0:
#         print(i,end=", ")
#     i+=1

#print all 4 digit numbers that contains digit '3' (in operator sequence)
# i=1000
# while i<=9999:
#     s=str(i)
#     if '3' in s:
#         print(s,end=", ")
#     i+=1

#Print those numbers that are divisible by 3 and 5 in the range (1,100)
# i=1
# while i<=100:
#     if i%3==0 and i%5==0:
#         print(i,end=", ")
#     i+=1
#
#1,4,9,16,25,36,49,64,81,100
# i=1
# while i<=10:
#         print(i**2,end=", ")
#         i+=1

#print all 3 digit numbers that contains digit '3' (in operator sequence)
i=100
while i<=999:
    s=str(i)
    if '3' in s:
        print(s,end=", ")
    i+=1