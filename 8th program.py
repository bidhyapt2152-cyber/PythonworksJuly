#Write a program to check whether the user entered number is a positive even or odd, negative even or odd
# n=int(input('Enter a number:'))
#
# if n>0:
#     print(f'{n} is positve')
#     if n%2==0:
#         print(f'{n} is even')
#     else:
#         print(f'{n} is odd')
# else:
#     print(f'{n} is negative')
#     if n%2!=0:
#         print(f'{n} is odd')
#     else:
#         print(f'{n} is even')

#check whether a number is divisible by 2 and 3

#check whether a number is divisible by 2 and not by 3
#check whether a number is divisible not by 2 and by 3
#check whether a number is not divisible by 2 and 3

n = int(input('Enter a number:'))

if n%2==0 and n%3==0:
    print('number is divisible by 2 and  by 3')
elif n%2==0 and n%3!=0:
     print('a number is divisible by 2 and not by 3')
elif n%2!=0 and n%3==0:
     print('number is divisible not by 2 and by 3')
elif n%2!=0 and n%3!=0:
     print('number is divisible not by 2 and not by 3')
else:
    print(n)