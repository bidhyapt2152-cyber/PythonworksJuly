
#1.write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

# w=float(input('Enter the Weight:'))
# h=float(input('Enter the Height'))
# BMI=w/(h**2)
#
# if BMI<=18.4:
#     print(f'{BMI} is Underweight')
# elif 18.5<=BMI<=24.9:
#     print(f'{BMI} is Normal')
# elif 25.0<=BMI<= 39.9:
#     print(f'{BMI} is Overweight')
# else:
#     print(f'{BMI} is Obese')

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# 2.Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
# code=int(input('1-->:battery based toys, 2-->:key-based toys, 3-->electrical charging based toys \n Enter the product code: '))
# price=int(input('Enter the actual price:'))
#
# if code==1:
#   if price>1000:
#        print(price-(price*0.1))
#   else:
#        print(price)
#
# if code==2:
#     if price>100:
#        print(price-(price*0.05))
#     else:
#         print(price)
#
# if code==3:
#      if price>500:
#          print(price-(price*0.1))
#      else:
#          print(price)
# else:
#    print('Error')


#3 FIZZBUZZ Problem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# n=int(input('Enter a number:'))
#
# if n%3==0 and n%5==0:
#     print('fizzbuzz')
# elif n%3==0 and n%5!=0:
#     print('fizz')
# elif n%3!=0 and n%5==0:
#     print('buzz')
# else:
#     print(n)
