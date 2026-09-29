# # # Prints: E, DD, CCC, BBBB, AAAAA
# n=ord('E')
#   for i in range(1,6):
#      for j in range(i,i+1):
#          print(chr(n),end='')
#          n=n-1
#     print()


for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()



for i in range(5, 0, -1):
    for j in range(6,i,-1):
        print(i,end=' ')
    print()