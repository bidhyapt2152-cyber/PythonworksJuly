
#d={'a':23,'b':25,'c':28,'d':30,'e':22}
#even values
# for i in d.values():
#        if i%2==0:
#         print(i)

#
#
#colors=['red','green','blue','orange','black']
#
# #starting letter
# for i in colors:
#       i=i[0]
#       print(i)
 #last letter
# for i in colors:
#        i=i[-1]
#        print(i)
#
# #reverse
# for i in colors:
#      i=i[::-1]
#      print(i)
#
# #all colors contains letter 'b'
# for i in colors:
#       if 'b' in i:
#        print(i)
#
#
# #Range function
#
# #100-200
# for i in range(100,201):
#   print(i,end=", ")
# #Range
# # 1,2,3,4,5
# for i in range(1,6):
#      print(i,end=", ")
#
# #1,3,5,7,9,11
# for i in range(1,13,2):
#      print(i,end=", ")
#
# #2,4,6,8,10
# for i in range(2,12,2):
#      print(i,end=", ")
#
# #100,200,300,400,500
# for i in range(100,600,100):
#      print(i,end=", ")

#
# #5,4,3,2,1
# for i in range(5,0,-1):
#      print(i,end=",")
#
# #3,6,9,12,15,18,21
# for i in range(3,24,3):
#       print(i, end=",")
# #
# #1,4,9,16,25,36
# for i in range(1,7):
#     i=i**2
#     print(i,end=",")
#
#


#print all 3 digit numbers(100-999)
# for i in range(100,999):
#      i+=1
#      print(i, end=",")

#print all numbers divisible by 3 in the range 100-200
# for i in range(100,201):
#      if i%3==0:
#            print(i, end=",")

#1,8,27,64,125
for i in range(1,6):
     i=i**3
     print(i, end=",")