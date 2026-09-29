#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end='')
#         k=k+1
#     print()
#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end='')
#     k=k+1
#     print()

#
# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end='')
#         k=k+1
#     print()

#l=[23,65,42,80,56,41]
#print all even numbers
# for i in l:
#     if(i%2==0):
#         print(i)
#print all prime numbers

# for i in l:
#
#         for j in range(2,i):
#             if i%j==0:
#
#                 break
#         else:
#                 print(i)

#print all prime numbers in the range(1,100)
# for i in range(1,100):
#
#         for j in range(2,i):
#             if i%j==0:
#
#                 break
#         else:
#                 print(i)

#print all amstrong numbers in the range(100,1000)
for i in range(100,1000):
    s=str(i)
    l=len(s)
    sum=0

    for j in s:
        sum=sum+int(j)**l

    if sum==i:
        print(i)