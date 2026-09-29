#count of those three digit number that contains digit '3'
#count=0 #Initializing with zero to block garbage values, for programs with sum and count
# i=100                       #Sets the starting number. 100 is the very first 3-digit integer.
# while i<999:                #Spans a loop that runs continuously as long as i <=999 (meaning it stops tracking after checking 998).
#     s=str(i)                #Converts the numeric math integer i into a text string s. Python cannot look inside an integer to find individual digits.
#     if '3' in s:
#         count=count+1
#     i+=1                    #Moves the loop forward to the next sequential integer.
# print(count)


#count of those numbers divisible by 7 or 3 in the range (200,300)
# count=0
# i=200
# while i<=300:
#
#
#     if i%7==0 or i%3==0:
#         count = count + 1
#     i += 1
#
# print(count)


#count the odd numbers that are divisible by 5 in the range (1,100)
# count=0
# i=1
# while i<100:
#
#
#     if i%2!=0 and i%5==0:
#         count = count + 1
#     i += 1
# print(count)

# count all palindrome number in the range(1,1000)
# count=0
# i=1
# while i<=1000:
#       s=str(i)
#     if(s==s[::-1]):
#         count = count + 1
#     i+=1
# print(count)

#count of numbers divisible by 3 in the range(1,50)
# count=0
# i=1
# while i<=50:
#
#      if i%3==0:
#        count = count + 1
#      i += 1
#
# print(count)

#Find the sum of first 5 numbers

# s=0
# i=1
# while i<=5:
#     s+=i
#     i+=1
# print(s)


#Sum of those numbers  that are divisible by 3 in the range (1,50)
# s=0
# i=1
# while i<=50:
#     if i%3==0:
#         s+=i
#     i+=1
# print(s)



# sum of all 3 digit numbers
# s=0
# i=100
# while i<=999:
#     s+=i
#     i+=1
# print(s)

# sum of first 10 even numbers
# s=0
# i=2
# while i<=20:
#     s+=i
#     i+=2
# print(s)


#Find the product of first 5 numbers
# p=1
# i=1
# while i<=5:
#     p*=i
#     i+=1
# print(p)

# product of first 10 odd numbers
# p=1
# i=1
# while i<=20:
#     p*=i
#     i+=2
# print(p)


#Product of  numbers  that contains digit 3 in the range(1,50)
# p=1
# i=1
# while i<=50:
#
#     if '3' in str(i):
#         p*=i
#     i+=1
# print(p)


#Factorial of a number entered by user 5!
# n=int(input('Enter the number:'))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#
#     i=i+1
# print(fact)

#multiplication table of a number upto 10
n=int(input('Enter input :'))

i=1
while i<=10:

    print(f'{i}   *  {n} = {n*i}')
    i=i+1

#sum of digit 135
n=int(input('Enter number:'))
