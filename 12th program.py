colors=['black','red','green','blue','orange','yellow']
# #print each color
# for i in colors:
#     print(i)

#colors containing letter 'b'
# for i in colors:
#     if 'b' in i:
#         print(i)

#colors starting with letter 'g'
# for i in colors:
#     if i[0]=='g':
#         print(i)

#colors end with 'e'
# for i in colors:
#     if i[-1]=='e':
#         print(i)

#First color starting with 'b'
# for i in colors:
#     if i[0]=='b':
#         print(i)
#         break


#all colors except color starting with 'b'
# for i in colors:
#     if i[0]!='b':
#         print(i)


   #Using loop control statements
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i)

#l=[23,45,12,78,90,51,75]
#print all numbers
# for i in l:
#     print(i)

#all even numbers
# for i in l:
#     if i%2==0:
#         print(i)

# those numbers divisible by 5
# for i in l:
#     if i%5==0:
#         print(i)

#stop the loop if i>50
# for i in l:
#     if i>50:
#         continue
#     print(i)

#Skip all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)

#print the first even number whose value is grater than 50
# for i in l:
#     if i%2==0 and i>50:
#         print(i)
#         break

#count of all even numbers
# c=0
# for i in l:
#     if i%2==0:
#         c+=1
# print(c)

#sum list
# s=0
# for i in l:
#     s+=i
# print(s)

#product of list
# p=1
# for i in l:
#     if i%2!=0:
#         p*=i
# print(p)

l=[1,2,3,4,5]
#print numbers at even index position


# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])

#         OR
#
# for number in l[::2]:
#     print(number)

#print numbers at odd index position
# for i in range(len(l)):
#     if i%2!=0:
#         print(l[i])

#print each digit in a number
# n=1234
# s=str(n)
# for i in s:
#     print(i)

#sum of digits in a number
# n=1234
# s=str(n)
# sums=0
# for i in s:
#     sums += int(i)   #i value should be integer while doing operations
# print(sums)

#products of digits in a number
n=1234
s=str(n)
p=1
for i in s:
    p*= int(i)
print(p)
