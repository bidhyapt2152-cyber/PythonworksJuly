#Write a program to calculate  electricity bill based on the following criteria
#Units consumed(units)   Rates per unit(Rs)
      #   100                  0
      # 100-200                5
      # 200-300                10
      # Above 300              15
#Qn. 325 units
# 100*0
# 100*5
# 100*10
# 25*25

# Units_consumed=int(input('Units Consumed'))
#
# if Units_consumed<=100:
#     bill=0
#
# elif (Units_consumed-100)>100 and (Units_consumed-100)<=200:
#     bill=0+(Units_consumed-100)*5
#
# elif (Units_consumed-200)>200 and (Units_consumed-200)<=300:
#     bill=0+((Units_consumed-100)*5)+(Units_consumed-200)*10
# else:
#     bill = 0+((Units_consumed - 100)* 5)+((Units_consumed - 200)*10)+(Units_consumed - 300)*15
#     print(bill)

# unit=int(input("Enter the number of units consumed"))
# if unit<=100:
#     bill=0
#     print("Bill is",bill)
# elif unit>100 and unit<=200:
#     bill=0+(unit-100)*5
#     print("Bill is", bill)
# elif unit>200 and unit<=300:
#     bill=0+500+(unit-200)*10
#     print("Bill is", bill)
# else:
#     bill=0+500+1000+(unit-300)*15
#     print("Bill is", bill)

#Write a program to check whether the user entered digit is two digit or three digit or four digit number

# n = input('Enter the number: ')
#
#
# if 10 <= n <= 99:
#     print(f'{n} is a two digit number')
# elif 100 <= n <= 999:
#     print(f'{n} is a three digit number')
# else:
#     print(f'{n} is a four digit number')

# a=input('Enter a number') #input text directly into a number using int(),  a number object has no length property
# if len(a)==2:
#      print(f"{a} is 2 digit")
# elif len(a)==3:
#      print(f"{a} is 3 digit")
# else:
#     print(f"{a} is 4 digit")

#2. Write a basic calculator program to perform arithmetic operations
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# operator=input("enter the operation")
# if operator=='+':
#     Ans=num1+num2
#     print("Answer is",Ans)
# elif operator=='-':
#     Ans=num1-num2
#     print("Answer is", Ans)
# elif operator=='*':
#     Ans=num1*num2
#     print("Answer is", Ans)
# elif operator=='/':
#     Ans=num1/num2
#     print("Answer is", Ans)
# elif operator=='%':
#     Ans=num1%num2
#     print("Answer is", Ans)
# elif operator=='//':
#     Ans=num1//num2
#     print("Answer is", Ans)
# else:
#     print("error")

#3 Write a program to print the number of days in a month
# n=input('Enter the month:')
# l1=['January','March','July','October','August','December']
# l2=['June','April','November''September']
# l3=['February']
# if n in l1:
#     print(f'{n} has 31 days')
# elif n in l2:
#     print(f'{n} has 30 days')
# else:
#     print(f'{n} has 28/29 days')

#4. Write a program to print the grades based on the following criteria: % IS taken from user
# 91-100          Grade A
# 81-90           Grade B
# 71-80           Grade C
# 61-70           Grade D
# Below 61        Grade E
n=int(input('Percentage obtained'))
if 91<=n<=100:
    print('Grade A')
elif 81<=n<=90:
    print('Grade B')
elif 71<=n<=80:
    print('Grade C')
elif 61<=n<=70:
    print('Grade D')
else:
    print('Grade E')
